# 🚀 Sales Streaming Medallion Pipeline

An end-to-end data engineering project demonstrating incremental data ingestion, stream processing, data quality validation, and medallion architecture using **AWS S3, Databricks Auto Loader, PySpark, Delta Lake, and Databricks Asset Bundles**.

The project ingests sales data from cloud storage, processes it through Bronze, Silver, and Gold layers, handles invalid records through a quarantine process, and makes the processed data available for analytics.

It also demonstrates how to organise and deploy Databricks resources using **Databricks Asset Bundles (DAB)** instead of relying only on manual workspace configuration.

---

## 📌 1. Project Overview

In real-world data engineering environments, data arrives continuously or incrementally from different source systems. Data engineers need reliable ingestion mechanisms, structured transformations, data quality checks, and monitoring to ensure that downstream analytics receive trustworthy data.

This project implements a sales data pipeline using the Medallion Architecture.

### Key objectives

- Ingest sales data from Amazon S3 using Databricks Auto Loader.
- Support incremental file ingestion.
- Build Bronze, Silver, and Gold data layers.
- Apply data transformations using PySpark and Spark SQL.
- Implement data quality validations and quarantine invalid records.
- Store processed data in Delta Lake tables.
- Orchestrate pipeline execution using Databricks resources.
- Deploy and manage Databricks resources using Databricks Asset Bundles.
- Monitor pipeline execution through event logs and job run details.
- Present analytical results through a Databricks AI/BI dashboard.

---

## 🏗️ 2. Architecture

The project follows a Medallion Architecture, where data is progressively refined through three layers.

```text
             AWS S3
               |
       Incoming Sales Data
               |
               v
       Databricks Auto Loader
               |
               v
       +---------------+
       | Bronze Layer  |
       | Raw Data      |
       +---------------+
               |
               v
       +---------------+
       | Silver Layer  |
       | Cleaned Data  |
       | Validations   |
       +---------------+
          |         |
          |         +------------------+
          v                            v
   +---------------+           +----------------+
   | Gold Layer    |           | Quarantine     |
   | Aggregations  |           | Invalid Records|
   +---------------+           +----------------+
          |
          v
    AI/BI Dashboard
```

### Medallion layers

| Layer | Purpose |
|---|---|
| Bronze | Ingest and preserve raw source data |
| Silver | Clean, validate, and prepare data for downstream processing |
| Gold | Produce business-level aggregated and analytical data |
| Quarantine | Isolate invalid records for investigation instead of allowing them into valid processing |

---

## ☁️ 3. Data Ingestion – AWS S3 and Auto Loader

Amazon S3 is used as the cloud storage source for incoming data.

Databricks Auto Loader is used to discover and incrementally ingest new files from cloud storage.

### Ingestion workflow

1. Source files are placed in the S3 incoming directory.
2. Auto Loader discovers new files.
3. Data is ingested into the Bronze layer.
4. Schema tracking and checkpoint information support incremental processing.
5. Newly arriving files can be processed without reprocessing the entire source directory.

### Storage organisation

```text
s3://sales-streaming-medallion-pipeline-jhansi/
│
├── incoming/
│   ├── sales/
│   └── customer/
│
├── databricks_metadata/
│   └── sales_bundle_schema/
│
├── archive/
│
└── quarantine/
```

---

## 🥉 4. Bronze Layer – Raw Data Ingestion

The Bronze layer is the initial landing layer of the Medallion Architecture.

Responsibilities:

- Ingest source data using Auto Loader.
- Preserve the incoming data for downstream processing.
- Capture ingestion metadata where configured.
- Maintain schema and checkpoint information.
- Support incremental ingestion of newly arriving files.

The Bronze layer acts as the foundation for subsequent transformations.

**Output:** `sales_bronze`

---

## 🥈 5. Silver Layer – Data Transformation and Quality

The Silver layer prepares the ingested data for reliable downstream consumption.

Responsibilities:

- Apply data cleansing and transformation logic.
- Validate incoming records against defined data quality rules.
- Identify invalid records.
- Separate records that fail validation into quarantine.
- Maintain clean records for downstream processing.

### Data Quality and Quarantine

Data quality is an important part of this project.

Instead of allowing invalid records to flow into analytical tables, the pipeline identifies records that do not satisfy the configured validation rules and handles them separately.

This makes it easier to inspect rejected records and understand data quality issues.

**Output:** `sales_silver`

---

## 🥇 6. Gold Layer – Business-Ready Data

The Gold layer contains refined data prepared for analytical consumption.

Responsibilities:

- Apply business-level transformations.
- Aggregate processed sales data.
- Prepare analytical datasets.
- Support reporting and dashboard development.

**Output:** `sales_gold`

---

## 📊 7. Databricks AI/BI Dashboard

The Gold layer provides the analytical data used by the Databricks AI/BI dashboard.

The dashboard presents sales-related insights based on the processed pipeline data.

The screenshots in the repository demonstrate the dashboard output.

---

## ⚙️ 8. Databricks Asset Bundles – Deployment and Resource Management

A key feature of this project is the use of **Databricks Asset Bundles (DAB)** to organise, validate, deploy, and run Databricks resources.

Rather than manually creating and managing every resource in the workspace, the project uses a configuration-driven deployment approach.

### Why Databricks Asset Bundles?

- Define project resources as code.
- Keep pipeline and job configurations organised.
- Separate source code from resource definitions.
- Validate bundle configuration before deployment.
- Deploy resources to a selected workspace target.
- Run deployed jobs through the Databricks CLI.

### Bundle configuration – `databricks.yml`

The `databricks.yml` file is the central configuration file for the Asset Bundle.

It defines the bundle configuration, workspace target, and references to the project resources.

### Project resource organisation

The project uses the following structure:

```text
Sales-Streaming-Medallion-Pipeline/
│
├── resources/
│   └── Databricks resource definitions
│
├── src/
│   └── Pipeline source code
│
├── tests/
│   └── Project tests
│
├── Screenshots/
│   └── Execution evidence
│
├── databricks.yml
│
├── .gitignore
│
└── README.md
```

### Folder responsibilities

| Folder/File | Purpose |
|---|---|
| `databricks.yml` | Main Asset Bundle configuration |
| `resources/` | Databricks job and pipeline resource definitions |
| `src/` | Pipeline implementation and source code |
| `tests/` | Test and validation code |
| `Screenshots/` | Project execution and monitoring evidence |
| `.gitignore` | Excludes files that should not be committed |
| `README.md` | Project documentation |

### Deployment workflow

The Databricks Asset Bundle CLI is used to validate, deploy, and execute the project.

```bash
# Validate bundle configuration
databricks bundle validate -t dev

# Deploy resources to the development target
databricks bundle deploy -t dev

# Run the deployed job
databricks bundle run sales_streaming_medallion_job -t dev
```

The development target is configured in the bundle configuration.

This approach demonstrates infrastructure-as-code principles and repeatable deployment of Databricks resources.

---

## 📂 9. Databricks Resources

The project defines its Databricks resources through the Asset Bundle configuration.

| Resource | Name |
|---|---|
| Bundle | `sales_streaming_medallion_pipeline` |
| Target | `dev` |
| Catalog | `sales_streaming` |
| Schema | `sales_bundle` |
| Pipeline | `sales_streaming_medallion_pipeline_bundle` |
| Job | `sales_streaming_medallion_job` |
| Job task | `run_sales_pipeline` |

---

## 🔍 10. Monitoring and Execution

Pipeline execution is monitored using Databricks pipeline event logs and job run information.

The project includes evidence of:

- Pipeline graph and execution flow.
- Pipeline event logs.
- Successful pipeline execution.
- Job task execution details.
- Quarantined invalid records.
- Databricks Asset Bundle CLI operations.

These help demonstrate both the processing workflow and the deployment process.

---

## 📸 11. Project Execution Screenshots

The repository includes screenshots of the implementation and execution.

| Screenshot | Description |
|---|---|
| [Pipeline Graph](Screenshots/01_pipeline_graph.png) | Pipeline architecture and flow |
| [Pipeline Event Log 1](Screenshots/02_pipeline_event_log_1.png) | Pipeline event information |
| [Pipeline Event Log 2](Screenshots/02_pipeline_event_log_2.png) | Additional event log details |
| [Successful Pipeline Run](Screenshots/03_successful_pipeline_run.png) | Successful execution |
| [AI/BI Dashboard 1](Screenshots/04_ai_bi_dashboard_1.png) | Dashboard analytics |
| [AI/BI Dashboard 2](Screenshots/04_ai_bi_dashboard_2.png) | Additional dashboard view |
| [Databricks Bundle CLI](Screenshots/05_databrick_bundle_cli.png) | Asset Bundle CLI operations |
| [Quarantine Records](Screenshots/06_quarantine_invalid_records.png) | Invalid record handling |
| [Pipeline Run Log](Screenshots/07_pipeline_run_log.png) | Job execution details |
| [Quarantine Delta Table](Screenshots/08_quarantine_invalid_records_table.png) | Quarantined records |

---

## 🛠️ 12. Technology Stack

| Technology | Usage |
|---|---|
| Python | Pipeline development |
| PySpark | Distributed data processing |
| Apache Spark | Data transformation and processing |
| Databricks Auto Loader | Incremental file ingestion |
| Delta Lake | Reliable data storage |
| Medallion Architecture | Layered data processing |
| Amazon S3 | Cloud object storage |
| Databricks Workflows | Job orchestration |
| Databricks Asset Bundles | Resource configuration and deployment |
| Databricks CLI | Bundle validation, deployment, and execution |
| Databricks AI/BI | Data visualisation and analytics |
| Git and GitHub | Version control and project documentation |

---

## 💡 13. Key Data Engineering Concepts Demonstrated

- Incremental data ingestion using Auto Loader.
- Cloud object storage integration.
- Bronze, Silver, and Gold architecture.
- PySpark transformations.
- Delta Lake tables.
- Data quality validation.
- Invalid record handling and quarantine.
- Pipeline orchestration and monitoring.
- Configuration-driven deployment.
- Infrastructure as Code using Databricks Asset Bundles.
- Version control using Git and GitHub.

---

## 👩‍💻 14. Author

**Data Engineering Portfolio Project**

Developed as a hands-on project to demonstrate practical data engineering concepts using AWS and Databricks.

[GitHub Repository](https://github.com/Jhansisrani/Sales-Streaming-Medallion-Pipeline)
