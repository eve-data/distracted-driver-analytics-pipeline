# Distracted Driver Analytics Platform

## Overview

This project explores how driver monitoring data can be transformed into an end-to-end analytics and machine learning platform for identifying distracted driving behaviours.

The project combines:

- Python
- Databricks
- Delta Lake
- SQL
- MLflow
- PyTorch
- Power BI

Rather than focusing solely on image classification, the project aims to demonstrate how behavioural observations can be processed, enriched, classified and ultimately transformed into actionable safety insights.

## Project Objective

The long-term goal is to simulate a driver monitoring system capable of identifying potentially unsafe driving behaviours before they contribute to road incidents.

The project combines:

1. Driver behaviour classification using computer vision.
2. Experiment tracking and model evaluation using MLflow.
3. Data engineering using a Medallion Architecture (Bronze, Silver, Gold).
4. Reporting and business-focused analytics.

## Architecture

Raw Images
↓
Behaviour Classification Model (PyTorch)
↓
MLflow Experiment Tracking
↓
Predicted Behaviour Events
↓
Bronze Layer (Databricks)
↓
Silver Layer
↓
Gold Layer
↓
Reporting & Visualisation

## Dataset

Multi-Class Driver Behavior Image Dataset

Behaviour categories:

- Safe Driving
- Talking on Phone
- Texting on Phone
- Turning
- Other Activities

The dataset was originally created for computer vision classification rather than estimating real-world distracted driving prevalence.

Dataset distributions should therefore be interpreted as labelled training observations rather than representative population statistics.

## Data Model

### Bronze Layer

Raw image metadata extracted from the source dataset.

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

Risk categories were developed as part of this project and are not provided by the original dataset.

The `other_activities` class is assigned `unknown_risk` because it contains multiple behaviours with potentially different risk levels. The dataset does not provide sufficient detail to assign a reliable risk category.

## Machine Learning Layer

The machine learning component is designed to classify driver behaviours directly from image data.

Current technology stack:

- PyTorch
- Google Colab (Tesla T4 GPU)
- MLflow
- Databricks

Planned outputs:

- Behaviour predictions
- Model evaluation metrics
- Experiment tracking
- Behaviour event generation for downstream analytics

## Current Progress

### Data Engineering

✅ Dataset selected

✅ Metadata extraction process created

✅ 7,286 image records transformed into structured metadata

✅ Bronze table created in Databricks

✅ Silver layer created

✅ Behaviour groups implemented

✅ Risk categories implemented

✅ Silver layer documented and validated

### Machine Learning

✅ MLflow environment validated

✅ PyTorch environment validated

✅ Google Colab GPU environment configured

✅ Dataset ingestion proof of concept completed

⏳ Model training

⏳ Model evaluation

⏳ Prediction pipeline

### Analytics

⏳ Gold layer

⏳ Reporting model

⏳ Power BI dashboard

## Repository Structure

```text
.
├── README.md
├── create_metadata.py
└── .gitignore
```

## External Assets

The following project components are currently maintained outside the repository:

- Databricks notebooks
- Bronze and Silver Delta tables
- Source image dataset
- ML experiments
- Model training notebooks

## Lessons Learned

A key project finding was that the source dataset was designed for machine learning classification rather than measurement of distracted driving prevalence.

As a result, behaviour frequencies cannot be interpreted as real-world driving statistics. This significantly influenced the analytical design of the project and led to a stronger focus on behaviour classification, event generation and driver monitoring use cases.

## Data Quality Validation

A validation process was implemented prior to model training to verify image integrity across the dataset.

Results:

- Images checked: 7,286
- Corrupted images identified: 10
- Corrupted images removed from the training dataset

Corrupted files were detected using Python and PIL image verification before model development. Invalid images were isolated from the training dataset to prevent data loading failures during PyTorch model training.

This step helped establish a clean and reliable dataset for downstream machine learning workflows.
