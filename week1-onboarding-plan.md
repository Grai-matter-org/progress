# Week 1 Developer Onboarding Plan – Grai-Matter + Dandelion

This document outlines the tasks assigned to the Grai-Matter developer team during Week 1. The goal is to ensure every developer is fully onboarded into the Dandelion environment and familiarized with the Med/Surg Staffing Pilot dataset.

---

## Goals

- Gain access to the Dandelion AWS + SageMaker environment
- Understand how to navigate, query, and explore the dataset
- Validate ability to visualize and summarize key data tables
- Ensure all developers are ready to begin feature engineering and modeling in Week 2

---

## Developer Tasks

Each developer is expected to complete all of the following tasks independently.

---

### Task 1: Access the Environment

**Objective:** Log into the Dandelion-hosted SageMaker Studio environment

**Steps:**

- Use credentials and temporary password provided by Dandelion
- Update password and configure MFA
- Open SageMaker Studio in region `us-east-1`
- Launch your personal JupyterLab space

**Deliverable:**  
- Screenshot of successful login and SageMaker Studio dashboard

---

### Task 2: List and Preview Available Tables

**Objective:** Identify and view the available dataset files stored in S3

**Steps:**

- Run:
  ```bash
  aws s3 ls s3://customer-dc-grai-matter-prod/
  ```
- List all available tables
- Load `grai_matter_dim_patient` as a Pandas or DuckDB DataFrame

**Deliverable:**  
- Markdown or notebook cell listing the tables  
- `head()` or preview of at least one table

---

### Task 3: Load and Explore Core Tables

**Objective:** Understand the schema and content of major data tables

**Required Tables:**
- `DIM_PATIENT`
- `FCT_MEDICATION`
- `FCT_ENCOUNTERS`
- `DIM_MED_ADMIN`

**Deliverable:**  
Notebook with:
- Shape and column names for each table
- Number of unique patients
- Range of dates for encounters and medication orders
- Example plot (e.g., histogram of patient age)

---

### Task 4: Schema Mapping and Linkage

**Objective:** Understand how tables link together via keys

**Steps:**

- Read Grai-Matter data documentation (PDF)
- Identify and document join keys (e.g., `PRIMARY_PATIENT_IDENTIFIER`, `DH_ENCOUNTER_ID`)

**Deliverable:**  
- Short summary (Markdown or Notebook) of each table’s function
- Description of how the tables relate (e.g., patient → encounters → meds)

---

### Task 5: Package Import and Basic Querying

**Objective:** Test use of packages and execution of lightweight analysis

**Steps:**

- Install one new package using:
  ```bash
  !aws codeartifact login --tool pip ...
  !pip install [package-name]
  ```
- Run basic query: e.g., how many encounters per patient?

**Deliverable:**  
- Histogram or bar plot of encounter count distribution

---

### Task 6: Cost Management Protocol

**Objective:** Practice safe shutdown and backup to manage AWS costs

**Steps:**

- Use `simple-backup.sh` to back up local files
- Shut down all running instances at end of day

**Deliverable:**  
- Screenshot of S3 backup confirmation  
- Confirmation that workspace was shut down

---

## Evaluation Criteria

A developer is considered "on track" if they:

- Have access to the environment and can navigate SageMaker
- Have loaded and explored at least 4 tables
- Can summarize table schemas and data relationships
- Can produce basic visualizations or queries
- Understand how to back up and shut down to reduce cost

---

## Feedback

- Create a slide or Markdown cell summarizing Week 1 learning and challenges
- Propose one potential project idea or area of interest based on initial data exploration

---

For any questions or access issues, contact:  
customersuccess@dandelionhealth.ai and CC armend@dandelionhealth.ai
