# Week 2 Project Plan — Patient Journey Clustering (Grai‑Matter × Dandelion)

This plan assigns four parallel clustering approaches for patient journey analysis on the Dandelion Med/Surg Staffing Pilot dataset. Each approach includes inputs, steps, deliverables, and acceptance criteria. Assign one developer per approach.

---

## Objectives

- Produce four independent clustering pipelines for patient journeys.
- Generate comparable outputs (embeddings, cluster labels, diagnostics) to inform model selection in Week 3.
- Document preprocessing so downstream teams can reproduce results.

---

## Common Setup (All Developers)

- Data sources: DIM_PATIENT, FCT_ENCOUNTERS, FCT_ICD_CODES, FCT_MEDICATION, FCT_PROCEDURE_CODES, DIM_MED_ADMIN.
- Join key(s): PRIMARY_PATIENT_IDENTIFIER everywhere; DH_ENCOUNTER_ID for encounter‑level joins.
- Inclusion: patients with ≥2 encounters.
- Outputs folder conventions inside SageMaker workspace:
  - `outputs/{approach_name}/artifacts/` (models, pickles, duckdb files)
  - `outputs/{approach_name}/figures/`
  - `outputs/{approach_name}/tables/`
  - `outputs/{approach_name}/notebooks/`
- Repro: place a `requirements.txt` and `README.md` inside each `outputs/{approach_name}`.

---

## Approach A — Basic Static Clustering

**Owner:** Dev 1  
**Idea:** Aggregate journeys to fixed‑length vectors and cluster.

### Steps
1. Feature build: counts or TF‑IDF for ICD10, CPT/HCPCS, drug classes; encounter stats (length, gaps).  
2. Scale features (StandardScaler or MaxAbs).  
3. Cluster with K‑Means (k=3..15), Agglomerative (Ward), and DBSCAN (tune eps via k‑distance).  
4. Select best model via internal metrics.

### Deliverables
- `tables/cluster_assignments.csv` (patient_id, cluster, model_name).  
- `figures/top_features_per_cluster.png`, `figures/elbow_silhouette.png`.  
- `notebooks/approach_A_static_clustering.ipynb` (end‑to‑end).

### Acceptance Criteria
- ≥1 model with silhouette ≥ 0.10 and DB index ≤ 2.0.  
- Cluster summaries listing top 20 features per cluster (ICD, procedure, meds).

---

## Approach B — QNet Latent Trajectories → Distance Matrix → PCS → Clustering

**Owner:** Dev 2  
**Idea:** Encode sequences with QNet; cluster on latent geometry.

### Steps
1. Build event sequences (ordered by time): encounter type, ICD, CPT, med orders/admins; include time deltas.  
2. Train QNet to produce patient‑level latent vectors or trajectory embeddings.  
3. Compute pairwise distance (cosine or Euclidean) between patient embeddings.  
4. Apply Principal Coordinates Scaling (PCS) to 2D/3D for visualization.  
5. Cluster (DBSCAN or Agglomerative) on latent space or PCS coordinates.

### Deliverables
- `artifacts/qnet_model.*` and config.  
- `tables/distance_matrix.parquet` (sparse if needed).  
- `figures/pcs_2d_scatter.png` colored by cluster.  
- `notebooks/approach_B_qnet_pcs_clustering.ipynb`.

### Acceptance Criteria
- Distance matrix computed for full cohort or a justified stratified sample.  
- Clear cluster separation visible on PCS plot and silhouette ≥ 0.10.

---

## Approach C — Sequence Similarity (DTW/Soft‑DTW) + Spectral Clustering

**Owner:** Dev 3  
**Idea:** Compare journeys as sequences; cluster by spectral methods.

### Steps
1. Represent each patient journey as a sequence of event vectors (e.g., one‑hot/indices or compact embeddings).  
2. Compute pairwise similarity using DTW or Soft‑DTW (batched; approximate for scale).  
3. Convert to affinity matrix; run spectral clustering (tune number of clusters via eigengap).  
4. Summarize representative sequences per cluster.

### Deliverables
- `tables/affinity_or_distance_matrix.*`.  
- `figures/spectral_eigengap.png`, `figures/cluster_sequence_examples.png`.  
- `notebooks/approach_C_dtw_spectral.ipynb`.

### Acceptance Criteria
- Spectral clustering converges with stable eigengap justification.  
- Representative timelines visualized for ≥3 clusters.

---

## Approach D — Transformer Embeddings → UMAP → HDBSCAN

**Owner:** Dev 4  
**Idea:** Encode journeys with a transformer; density‑based clustering on reduced space.

### Steps
1. Tokenize events (ICD, CPT, drug class, encounter type) with positional/time‑gap encodings.  
2. Train or adapt an EHR‑transformer (BEHRT/Med‑BERT/LHM‑module) to output patient embeddings.  
3. Reduce with UMAP (n_neighbors=30, min_dist=0.1; log params).  
4. Cluster with HDBSCAN (min_cluster_size tuned; capture noise points).

### Deliverables
- `artifacts/transformer_checkpoint.*`.  
- `tables/embeddings.parquet`, `tables/cluster_labels.parquet`.  
- `figures/umap_scatter_hdbscan.png`.  
- `notebooks/approach_D_transformer_umap_hdbscan.ipynb`.

### Acceptance Criteria
- ≥2 non‑noise clusters identified by HDBSCAN with ≥50 patients each (or justified threshold).  
- UMAP plot and cluster interpretability tables (top codes per cluster).

---

## Cross‑Method Evaluation

**Owner:** Any (shared comparison notebook)  
1. Compute internal metrics for each method: silhouette, Davies–Bouldin, Calinski–Harabasz.  
2. Compute Adjusted Rand Index (ARI) pairwise across methods.  
3. Produce a consolidated report comparing cluster interpretability (diagnoses/procedures/meds, demographics).

**Deliverables**
- `notebooks/compare_methods.ipynb`.  
- `tables/metrics_summary.csv`, `tables/ari_matrix.csv`.  
- `figures/metrics_barplot.png`, `figures/ari_heatmap.png`.

---

## Timeline (Week 2)

- Day 1: finalize data schema, sampling strategy (if needed), and shared preprocessing.  
- Days 2–3: model training/fit per approach; interim metric dumps.  
- Day 4: refine hyperparameters; generate figures/tables.  
- Day 5: cross‑method comparison; publish report and recommend finalists for Week 3.

---

## Risk & Mitigations

- Pairwise distances may be O(N^2): use stratified sampling, blockwise computation, or approximate nearest neighbors.  
- Memory limits in SageMaker: switch to DuckDB/Polars, chunked reads, or scale instance temporarily.  
- Package access in air‑gapped env: install via CodeArtifact; document versions in `requirements.txt`.

---

## Repository Layout (suggested)

```
/projects/patient_journeys/
  preprocessing/
    build_patient_sequences.py
    build_static_features.py
  approaches/
    A_static_clustering/
    B_qnet_pcs/
    C_dtw_spectral/
    D_transformer_umap_hdbscan/
  compare/
    compare_methods.ipynb
  outputs/  (gitignored; mirrored to S3 via backup scripts)
  README.md
```

---

## Definition of Done

- Four notebooks run end‑to‑end, each with saved artifacts, tables, and figures.  
- Comparison notebook completed with metric tables and plots.  
- Short written recommendation (1–2 pages) on which approach(es) to advance in Week 3 and why.
