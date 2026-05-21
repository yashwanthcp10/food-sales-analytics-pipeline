# Food Sales Analytics Pipeline

Production-grade end-to-end Data Engineering pipeline using:

- Python
- GCP
- BigQuery
- GCS
- PySpark
- SQL

## Features

- Automated ingestion
- Data quality checks
- Retry mechanism
- Logging
- Idempotent processing
- Bronze/Silver/Gold architecture
- Monthly scheduling
- Archival strategy


# Architecture

```text
Incoming Files
      ↓
Validation Framework
      ↓
GCS Raw Bucket
      ↓
Bronze Layer
      ↓
Silver Layer
      ↓
Gold KPI Layer
      ↓
Dashboard Reporting
```

# Tech Stack

- Python
- Pandas
- PySpark
- GCP
- BigQuery
- GCS
- Airflow
- Docker
- GitHub Actions


# Features

- Automated ingestion
- Data validation
- Retry mechanism
- Idempotent processing
- Bronze/Silver/Gold architecture
- Airflow scheduling
- CI/CD integration
- Dockerized pipeline
- Automated archival

---

# Project Structure

```text
src/
tests/
configs/
airflow/
```

# How To Run

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start Pipeline

```bash
python -m src.ingestion.watch_folder
```

## Run Tests

```bash
pytest
```

---

# Scheduling

Airflow DAG runs monthly on 2nd day.

---

# CI/CD

GitHub Actions automatically runs tests on push.