# updated New target (Nov 14)

## Results so far
1. Plot ROC for n_encounter with long_stay defined to be 1,2,3,4,5 days as long stay cut points (5 curves)
2. Plot the AUV vs the 1,2,3,4,5 long-stay cut points
3. R2 for stay_durationin hospital, and indifferent units (bar plot: units vs R2)

## Procedure prediction

1. List the top (most frequent , say top 10) procedures
2. List the top most time consuming procedures
3. For each compute the distribution over patient (encounter specific) IC codes (using first 3 letters), demographics, age, sex 




# past target

1. Prediction model (regressor or classifer) for the number of encounters and number of encounter days
       + you cannot use features that are not known at encounter begin time
       +  figure out for each enounter the sum of total number fo prodecures and ic codes in all past encounters for teh same patienst, and use them as features
       +  similarly figure out the sum of all encounter days and number fo past encounters for the same patient and use them as features
Note: the key point is NOT to use data that is not available at the beginnning of teh current encounter
2. Find clusters in the expanded tabular data set created in 1. (the new dataset you have, expanded by including teh past aggregate data from previous encounters)

3. Make a time series of total number of encounters  in different units over time. Note, to do this, you need to find where each encounter strats and ends and add up the total number fo encounters at each day.


# progress
Track progress of analysis on Dandelion data

# current columns

```
['patient_id', 'n_encounters', 'icd10_codes_array',
       'icd_prefix_A41', 'icd_prefix_C18', 'icd_prefix_C34',
       'icd_prefix_C50', 'icd_prefix_C79', 'icd_prefix_D50',
       'icd_prefix_D64', 'icd_prefix_E03', 'icd_prefix_E10',
       'icd_prefix_E11', 'icd_prefix_E66', 'icd_prefix_E78',
       'icd_prefix_E83', 'icd_prefix_E86', 'icd_prefix_E87',
       'icd_prefix_F10', 'icd_prefix_F17', 'icd_prefix_F32',
       'icd_prefix_F33', 'icd_prefix_F41', 'icd_prefix_F43',
       'icd_prefix_G43', 'icd_prefix_G47', 'icd_prefix_G89',
       'icd_prefix_I10', 'icd_prefix_I21', 'icd_prefix_I25',
       'icd_prefix_I48', 'icd_prefix_I50', 'icd_prefix_I63',
       'icd_prefix_I73', 'icd_prefix_I82', 'icd_prefix_J18',
       'icd_prefix_J44', 'icd_prefix_J45', 'icd_prefix_J96',
       'icd_prefix_K21', 'icd_prefix_K57', 'icd_prefix_K59',
       'icd_prefix_K70', 'icd_prefix_K80', 'icd_prefix_K92',
       'icd_prefix_L03', 'icd_prefix_M17', 'icd_prefix_M19',
       'icd_prefix_M25', 'icd_prefix_M54', 'icd_prefix_M79',
       'icd_prefix_M86', 'icd_prefix_N17', 'icd_prefix_N18',
       'icd_prefix_N20', 'icd_prefix_N25', 'icd_prefix_N30',
       'icd_prefix_N39', 'icd_prefix_N40', 'icd_prefix_R00',
       'icd_prefix_R05', 'icd_prefix_R06', 'icd_prefix_R07',
       'icd_prefix_R09', 'icd_prefix_R10', 'icd_prefix_R11',
       'icd_prefix_R13', 'icd_prefix_R19', 'icd_prefix_R41',
       'icd_prefix_R42', 'icd_prefix_R53', 'icd_prefix_R60',
       'icd_prefix_R63', 'icd_prefix_R69', 'icd_prefix_R73',
       'icd_prefix_R79', 'icd_prefix_R91', 'icd_prefix_R93',
       'icd_prefix_S72', 'icd_prefix_S82', 'icd_prefix_U07',
       'icd_prefix_Z00', 'icd_prefix_Z01', 'icd_prefix_Z09',
       'icd_prefix_Z11', 'icd_prefix_Z12', 'icd_prefix_Z13',
       'icd_prefix_Z23', 'icd_prefix_Z48', 'icd_prefix_Z51',
       'icd_prefix_Z68', 'icd_prefix_Z79', 'icd_prefix_Z80',
       'icd_prefix_Z85', 'icd_prefix_Z86', 'icd_prefix_Z87',
       'icd_prefix_Z90', 'icd_prefix_Z91', 'icd_prefix_Z94',
       'icd_prefix_Z95', 'icd_prefix_Z96', 'icd_prefix_Z98',
       'icd_prefix_Z99', 'avg_los_days', 'max_los_days',
       'total_transfers', 'n_distinct_event_types', 'PATIENT_BIRTH_YEAR',
       'PATIENT_SEX', 'PATIENT_RACE_ETHNICITY', 'DECEASED_FLAG', 'age']

```

# additional variables needed

+ No. of days in Med Surge
+ No. of prescriptions
+ No. of administration of Rx
+ No. of imaging done
+ Was transfer needed for imaging (Boolean, 0 or 1 )
+ Total no. of procedures
+ Add procedure list

# Next steps
1. check variable definitions
2. Add the above variables

# Next steps
1. Fix table (make code arrays as tuples with time stamp
2. Add predictions for other variables aleady in the tabular dataset
3. Make a new tabulat data-table with "journey variables"

---

# Next step

# task 1
---
## ADT journey: 

```
patient: (dept/event,time_in), (dept/event, time_in),...
```

Event example:

+ admission
+ discharge

Example departments:
+ Emergency
+ preop
+ postop
+ ICU


# task 2
---
## Table update
+ make each row unique for distinct episodes
+ thus, table index will have non-unique entries for patient id

# task 3
---
## Model  quantized medsurg_stay_days_avg prediction

+ low: <= 2
+ high: rest


  
