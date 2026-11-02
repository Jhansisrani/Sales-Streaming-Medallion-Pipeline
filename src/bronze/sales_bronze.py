from pyspark import pipelines as dp
from pyspark.sql.functions import col, current_timestamp



@dp.table(
    name="sales_bronze",
    comment="Raw sales data ingested from AWS S3 using Auto Loader"
)
def sales_bronze():

    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "json")
        .option(
            "cloudFiles.schemaLocation",
            "s3://sales-streaming-medallion-pipeline-jhansi/databricks_metadata/sales_bundle_schema/"
        )
        .option("cloudFiles.schemaEvolutionMode", "addNewColumns")
        .option("rescuedDataColumn", "_rescued_data")
        .load(
            "s3://sales-streaming-medallion-pipeline-jhansi/incoming/sales/"
        )
        .withColumn("_ingested_at", current_timestamp())
        .withColumn("_source_file", col("_metadata.file_path"))
    )