# Distracted Driver Analytics Pipeline

## Overview

This project explores distracted driving behaviours using a modern driver behaviour image dataset.

The project focuses on building an end-to-end data and analytics platform using:

- Python
- Databricks
- Delta Lake
- SQL
- Power BI

Future project phases may incorporate machine learning and MLflow to support automated driver behaviour classification.

## Architecture

Raw Images  
↓  
Metadata Extraction (Python)  
↓  
Bronze Layer (Databricks)  
↓  
Silver Layer  
↓  
Gold Layer  
↓  
Power BI Dashboard

## Dataset

**Multi-Class Driver Behavior Image Dataset**

Behaviour categories:

- Safe Driving
- Talking on Phone
- Texting on Phone
- Turning
- Other Activities

## Data Model

### Bronze Layer

Raw image metadata extracted from the source image dataset.

Columns:

- image_name
- behaviour
- extension

### Silver Layer

Business enrichment layer that adds analytical classifications to behaviour observations.

Additional columns:

- behaviour_group
- risk_category

#### Important Note

Risk categories were created as part of this project and are not provided by the original dataset.

The `other_activities` class is assigned `unknown_risk` because it contains multiple behaviours with potentially different risk levels. The original dataset groups several activities under a single label, making it impossible to assign a reliable risk category without additional information.

## Current Progress

✅ Dataset selected

✅ Metadata extraction process created

✅ 7,286 image records transformed into structured metadata

✅ Bronze table created in Databricks

✅ Initial SQL exploration completed

✅ Silver layer created with behaviour groups and risk categories

✅ Driver monitoring business classifications implemented

✅ Silver layer documented and validated

## Repository Structure

```text
.
├── README.md
├── create_metadata.py
└── .gitignore
```

### External Assets

The following project components are currently maintained outside the repository:

- Databricks notebooks
- Bronze and Silver Delta tables
- Source image dataset

## Project Goal

The objective of this project is not to analyse image quality or estimate real-world distracted driving prevalence.

Instead, the project demonstrates how driver monitoring observations can be transformed into an analytics-ready data platform using a Bronze, Silver and Gold architecture.

The long-term goal is to simulate a driver monitoring system capable of identifying distracted driving behaviours and supporting downstream risk analysis, reporting and dashboarding.
