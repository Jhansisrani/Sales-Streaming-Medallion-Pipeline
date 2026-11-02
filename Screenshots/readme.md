# Sales Streaming Medallion Pipeline – Execution Screenshots

This folder contains screenshots demonstrating the implementation, execution, data quality validation, and output of the Sales Streaming Medallion Pipeline built using Databricks Asset Bundles.

## 1. Pipeline Architecture and Execution

- **Pipeline Graph:** Shows the Bronze, Silver, Gold and Quarantine data processing flow.
- **Pipeline Details:** Displays pipeline configuration and execution information.
- **Successful Run:** Demonstrates successful execution of the Databricks pipeline.
- **Run History:** Shows pipeline execution history, duration and status.

## 2. Event Logs and Monitoring

- **Event Log:** Shows pipeline initialization, resource allocation, table setup and processing events.
- **Error Events:** Captures error events for troubleshooting and debugging.
- **Successful Events:** Demonstrates successful pipeline execution.

## 3. Data Quality and Quarantine

A separate test batch containing six sales records was generated and uploaded to the existing S3 incoming folder.

The test batch included:

| Test scenario | Expected result |
|---|---|
| Valid sales record | Accepted |
| Zero quantity | Invalid |
| Negative unit price | Invalid |
| Incorrect total amount | Invalid |
| Missing product name | Invalid |
| Missing city | Invalid |

The pipeline processes incoming records through Bronze and applies data quality validations in Silver.

Invalid records are directed to the Quarantine table for further investigation, while valid records continue through the Silver and Gold layers.

- **Quarantine Table:** Shows captured invalid records in Databricks Catalog Explorer.
- **Silver Table:** Shows cleaned and validated sales records.

## 4. Gold Layer

- **Gold Table:** Shows the transformed and aggregated sales output.
- **Materialized View Graph:** Demonstrates the available dataset dependencies and transformations.

## 5. Analytics Dashboard

- **AI/BI Dashboard:** Demonstrates sales analytics and visualizations generated using the Gold layer.

## Technology Stack

- Databricks
- PySpark
- Structured Streaming
- Auto Loader
- Delta Lake
- Lakeflow Spark Declarative Pipelines
- Lakeflow Jobs
- Databricks Asset Bundles
- AWS S3
- Python
- Git and GitHub

## Project Objective

To build an incremental sales data ingestion and transformation pipeline using a Medallion Architecture, implement data quality validations, isolate invalid records through quarantine handling, and provide aggregated Gold-layer data for analytics.
