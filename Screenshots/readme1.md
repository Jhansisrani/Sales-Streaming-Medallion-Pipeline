# Sales-Streaming-Medallion-Pipeline
# 📸 Project Execution Screenshots

This folder contains screenshots demonstrating the implementation, execution, monitoring, and output of the **Sales Streaming Medallion Pipeline** built using Azure/AWS storage integration, Databricks Auto Loader, Delta Lake, and Databricks Asset Bundles.

## 1. Pipeline Architecture

### 01 – Pipeline Graph
![Pipeline Graph](01_pipeline_graph.png)

Overview of the Databricks pipeline structure and the execution flow across the Bronze, Silver, and Gold layers.

## 2. Pipeline Monitoring

### 02 – Pipeline Event Log
![Pipeline Event Log 1](02_pipeline_event_log_1.png)

First view of the pipeline event log, showing execution events and pipeline activity.

![Pipeline Event Log 2](02_pipeline_event_log_2.png)

Additional event log details for monitoring pipeline execution and processing activity.

### 03 – Successful Pipeline Run
![Successful Pipeline Run](03_successful_pipeline_run.png)

Evidence of a successful pipeline execution.

### 07 – Pipeline Run Log
![Pipeline Run Log](07_pipeline_run_log.png)

Task-level execution details and run status for the Databricks pipeline job.

## 3. Data Quality and Quarantine

### 06 – Quarantine: Invalid Records
![Quarantine Invalid Records](06_quarantine_invalid_records.png)

Screenshot demonstrating the handling of invalid records through the quarantine process.

### 08 – Quarantine Records Table
![Quarantine Records Table](08_quarantine_invalid_records_table.png)

Quarantined records stored in a Delta table for inspection and further analysis.

## 4. Analytics Dashboard

### 04 – AI/BI Dashboard
![AI BI Dashboard 1](04_ai_bi_dashboard_1.png)

First view of the dashboard presenting sales-related analytics.

![AI BI Dashboard 2](04_ai_bi_dashboard_2.png)

Additional dashboard view highlighting the analytical outputs of the pipeline.

## 5. Deployment and CI/CD

### 05 – Databricks Asset Bundles CLI
![Databricks Bundle CLI](05_databrick_bundle_cli.png)

Command-line evidence of Databricks Asset Bundles operations used to validate, deploy, and run the project in the development environment.

---

**Note:** These screenshots document the implemented project workflow and its execution evidence. Refer to the main [README](../README.md) for the project overview, architecture, technologies, and implementation details.
