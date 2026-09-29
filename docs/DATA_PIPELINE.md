# Data Pipeline Documentation

## Purpose

This document describes the end-to-end data pipeline for the Iris dataset.

The pipeline consists of four stages:

1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Data Validation

The complete pipeline is automated using DVC.

---

## Pipeline Flow

```text
Data Collection
      ↓
Raw Data
      ↓
Preprocessing
      ↓
Processed Data
      ↓
Feature Engineering
      ↓
Feature Dataset
      ↓
Validation