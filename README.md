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

Rather than focusing solely on image classification, the project demonstrates how behavioural observations can be processed, enriched, classified and ultimately transformed into actionable safety insights.

---

# Project Objective

The long-term goal is to simulate a driver monitoring system capable of identifying potentially unsafe driving behaviours before they contribute to road incidents.

The project combines:

1. Driver behaviour classification using computer vision.
2. Experiment tracking and model evaluation using MLflow.
3. Data engineering using a Medallion Architecture (Bronze, Silver, Gold).
4. Reporting and business-focused analytics.

---

# Architecture

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

---

# Dataset

**Multi-Class Driver Behavior Image Dataset**

Behaviour categories:

- Safe Driving
- Talking on Phone
- Texting on Phone
- Turning
- Other Activities

The dataset was originally created for computer vision classification rather than estimating real-world distracted driving prevalence.

Dataset distributions should therefore be interpreted as labelled training observations rather than representative population statistics.

---

# Data Quality Validation

A validation process was implemented prior to model training to verify image integrity across the dataset.

Results:

- Images checked: 7,286
- Corrupted images identified: 10
- Corrupted images removed from the training dataset

Corrupted files were detected using Python and PIL image verification before model development. Invalid images were isolated from the training dataset to prevent data loading failures during PyTorch model training.

This step helped establish a clean and reliable dataset for downstream machine learning workflows.

---

# Data Model

## Bronze Layer

Raw image metadata extracted from the source dataset.

Columns:

- image_name
- behaviour
- extension

---

## Silver Layer

Business enrichment layer that adds analytical classifications to behaviour observations.

Additional columns:

- behaviour_group
- risk_category

### Important Note

Risk categories were developed as part of this project and are not provided by the original dataset.

The `other_activities` class is assigned `unknown_risk` because it contains multiple behaviours with potentially different risk levels. The dataset does not provide sufficient detail to assign a reliable risk category.

---

# Machine Learning Layer

The machine learning component classifies driver behaviours directly from image data.

Technology Stack:

- PyTorch
- Google Colab (Tesla T4 GPU)
- MLflow
- Databricks

---

# MobileNetV2 Baseline Model

The first baseline model was implemented using MobileNetV2.

Dataset split:

| Dataset | Images |
|----------|---------:|
| Training | 5,093 |
| Validation | 1,091 |
| Test | 1,092 |

---

## Baseline Results

| Metric | Value |
|----------|----------:|
| Test Accuracy | 93.68% |
| Test Loss | 0.1809 |

---

## Model Evaluation

Artifacts generated:

- Confusion Matrix
- Classification Report
- Prediction Table
- MLflow Experiment Run

### Classification Performance

| Class | Precision | Recall | F1 Score |
|----------|----------:|----------:|----------:|
| other_activities | 0.77 | 0.95 | 0.85 |
| safe_driving | 0.95 | 0.92 | 0.94 |
| talking_phone | 0.98 | 0.94 | 0.96 |
| texting_phone | 1.00 | 0.95 | 0.97 |
| turning | 0.99 | 0.92 | 0.95 |

Overall Accuracy: **93.68%**

---

## Key Findings

- MobileNetV2 achieved strong performance across all behaviour categories.
- Phone-related distraction behaviours were identified with particularly high accuracy.
- The most challenging class was `other_activities`.
- The most common classification errors occurred between:
  - other_activities and safe_driving
  - other_activities and turning
- The model occasionally produced high-confidence misclassifications, making confidence analysis an important part of downstream analytics.

---

# Current Progress

## Data Engineering

✅ Dataset selected

✅ Metadata extraction process created

✅ 7,286 image records transformed into structured metadata

✅ Bronze table created in Databricks

✅ Silver layer created

✅ Behaviour groups implemented

✅ Risk categories implemented

✅ Silver layer documented and validated

---

## Machine Learning

✅ MLflow environment configured

✅ PyTorch environment configured

✅ Google Colab GPU environment configured

✅ Dataset ingestion completed

✅ MobileNetV2 baseline model trained

✅ Model evaluation completed

✅ Confusion matrix generated

✅ Classification 
