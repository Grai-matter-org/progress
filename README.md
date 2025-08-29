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
   

  
