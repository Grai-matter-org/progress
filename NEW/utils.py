import numpy as np
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import GroupKFold, train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import mean_absolute_error, r2_score, roc_auc_score, average_precision_score, classification_report
from lightgbm import LGBMRegressor, LGBMClassifier
import matplotlib.pyplot as plt


def build_preproc(df, feature_list):
    # separate categorical and numeric
    cat_cols = [c for c in feature_list if df[c].dtype == 'object']
    num_cols = [c for c in feature_list if c not in cat_cols]

    preproc = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_cols),
            ('num', 'passthrough', num_cols)
        ],
        remainder='drop'
    )
    return preproc, cat_cols, num_cols

def fit_and_eval_cls(
        feature_list: list, y_col: str, 
        label: str, df_train: pd.DataFrame, df_test,
        use_additional=False, additional_columns=[]
        ):
    use_cols = feature_list.copy()
    preproc, cat_cols, num_cols = build_preproc(df_train, use_cols)
    if use_additional:
        use_cols += additional_columns
    clf = LGBMClassifier(
        metric='binary_logloss',
        class_weight='balanced',
        subsample=0.7,
        reg_lambda=1.0,
        reg_alpha=1.0,
        n_estimators=300,
        min_child_samples=5,
        learning_rate=np.float64(0.01),
        num_leaves=31,
        colsample_bytree=1,
    )
    pipe = Pipeline([
        ('prep', preproc),
        ('lgbm', clf)
    ])
    X_tr, y_tr = df_train[use_cols], df_train[y_col]
    X_te, y_te = df_test[use_cols],  df_test[y_col]

    pipe.fit(X_tr, y_tr)
    proba = pipe.predict_proba(X_te)[:,1]
    # prec, rec, thresh = precision_recall_curve(y_te, proba)
    # f1 = 2 * (prec * rec) / (prec + rec + 1e-9)

    # best_idx = f1.argmax()
    # best_thresh = thresh[best_idx]
    cost_fn = 3
    cost_fp = 2

    # thresholds = np.linspace(0, 1, 500)
    # costs = []

    # for t in thresholds:
    #     pred = (proba >= t).astype(int)
    #     fn = ((y_te == 1) & (pred == 0)).sum()
    #     fp = ((y_te == 0) & (pred == 1)).sum()
    #     costs.append(cost_fn * fn + cost_fp * fp)

    best_thresh = 0.70 # thresholds[np.argmin(costs)]
    pred  = (proba >= best_thresh).astype(int)
    print(f"Best threshold for {y_col}: {best_thresh:.3f}")

    auc = roc_auc_score(y_te, proba)
    ap  = average_precision_score(y_te, proba)
    print(f"[{label}] Classifier {y_col}: AUC={auc:.3f}, PR-AUC={ap:.3f}")
    print(classification_report(y_te, pred, digits=3))
    return pipe, proba, {'AUC': auc, 'PR_AUC': ap}, best_thresh


def to_long_with_offsets(df, id_col="encounter_id"):
    base = df[[id_col, "encounter_start_dt", "proc_times_seq_str", "proc_descs_seq_str"]].copy()

    base["encounter_start_dt"] = pd.to_datetime(base["encounter_start_dt"], errors="coerce")
    if pd.api.types.is_datetime64tz_dtype(base["encounter_start_dt"]):
        base["encounter_start_dt"] = base["encounter_start_dt"].dt.tz_convert(None)

    base["proc_times_list"] = base["proc_times_seq_str"].fillna("").astype(str).str.split("|")
    base["proc_descs_list"] = base["proc_descs_seq_str"].fillna("").astype(str).str.split("|")

    long = base.drop(columns=["proc_times_seq_str", "proc_descs_seq_str"]).explode(
        ["proc_times_list", "proc_descs_list"], ignore_index=True
    )

    long = long[(long["proc_times_list"] != "") & (long["proc_descs_list"] != "")].copy()

    long["proc_time"] = pd.to_datetime(long["proc_times_list"], errors="coerce")
    if pd.api.types.is_datetime64tz_dtype(long["proc_time"]):
        long["proc_time"] = long["proc_time"].dt.tz_convert(None)

    long["proc_desc"] = long["proc_descs_list"]
    long["days_after_start"] = (long["proc_time"] - long["encounter_start_dt"]).dt.days

    long["proc_idx"] = long.groupby(id_col).cumcount()

    return long[[id_col, "encounter_start_dt", "proc_idx", "proc_desc", "proc_time", "days_after_start"]]


def build_day_level_df(df, long_df, procedure, max_day=7, id_col="encounter_id"):
    base = df.copy()

    days = (
        base[[id_col]]
        .drop_duplicates()
        .assign(key=1)
        .merge(pd.DataFrame({"day": range(max_day), "key": 1}), on="key")
        .drop(columns="key")
    )

    proc_days = (
        long_df[long_df["proc_desc"] == procedure]
        [[id_col, "days_after_start"]]
        .rename(columns={"days_after_start": "day"})
        .assign(occurs=1)
    )

    out = (
        days
        .merge(proc_days, on=[id_col, "day"], how="left")
        .fillna({"occurs": 0})
        .merge(base, on=id_col, how="left")
    )

    out["procedure"] = procedure
    return out
