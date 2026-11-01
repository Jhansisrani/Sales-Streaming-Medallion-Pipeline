# Lakeflow Spark Declarative Pipelines – UI-Based Approach

## Overview
Implemented a Medallion Architecture pipeline using Databricks Lakeflow Spark Declarative Pipelines and Python decorators.

## Implementation
- Created an ETL pipeline through the Databricks UI.
- Used `@dp.table` to define streaming tables.
- Used `@dp.materialized_view` to define aggregated Gold data.
- Implemented Bronze ingestion using Auto Loader from AWS S3.
- Applied Silver data cleaning and validation.
- Created a quarantine table for invalid records.
- Built Gold-level sales aggregations.

## Pipeline Results
The successful pipeline run produced:
- Bronze: 125 records
- Silver: 125 records
- Quarantine: 0 records
- Gold: 16 aggregated rows

See the `screenshots/` folder for the successful pipeline execution.

## Key Learning
Understood how Python decorators define datasets and dependencies in Lakeflow Spark Declarative Pipelines.
