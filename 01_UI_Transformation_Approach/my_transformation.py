
from pyspark import pipelines as dp
from pyspark.sql.functions import (
    col,
    trim,
    current_timestamp,
    expr,
    when,
    count,
    sum as spark_sum,
    avg,
    round
)


# --------------------------------------------------
# BRONZE: Ingest raw Sales JSON using Auto Loader
# --------------------------------------------------

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
            "s3://sales-streaming-medallion-pipeline-jhansi/databricks_metadata/sales_schema/"
        )
        .option("cloudFiles.schemaEvolutionMode", "addNewColumns")
        .option("rescuedDataColumn", "_rescued_data")
        .load(
            "s3://sales-streaming-medallion-pipeline-jhansi/incoming/sales/"
        )
    )


# --------------------------------------------------
# COMMON FUNCTION: Standardise and validate Sales
# --------------------------------------------------

def prepare_sales(df):

    return (
        df
        .withColumn("product_name", trim(col("product_name")))
        .withColumn("city", trim(col("city")))
        .withColumn("customer_id", trim(col("customer_id")))
        .withColumn("quantity", col("quantity").cast("int"))
        .withColumn("unit_price", col("unit_price").cast("double"))
        .withColumn("total_amount", col("total_amount").cast("double"))
        .withColumn("sale_timestamp", col("sale_timestamp").cast("timestamp"))
        .withColumn("_processed_at", current_timestamp())
    )


def validate_sales(df):

    return (
        col("sale_id").isNotNull()
        & col("customer_id").isNotNull()
        & (col("customer_id") != "")
        & col("quantity").isNotNull()
        & (col("quantity") > 0)
        & col("unit_price").isNotNull()
        & (col("unit_price") > 0)
        & col("total_amount").isNotNull()
        & (col("total_amount") > 0)
        & (
            expr("ABS(total_amount - (quantity * unit_price)) < 0.01")
        )
        & col("product_name").isNotNull()
        & (col("product_name") != "")
        & col("city").isNotNull()
        & (col("city") != "")
        & col("sale_timestamp").isNotNull()
    )


# --------------------------------------------------
# SILVER: Clean and validated Sales records
# --------------------------------------------------

@dp.table(
    name="sales_silver",
    comment="Cleaned and validated sales records"
)
def sales_silver():

    df = prepare_sales(
        spark.readStream.table("sales_bronze")
    )

    return df.filter(validate_sales(df))


# --------------------------------------------------
# QUARANTINE: Capture rejected Sales records
# --------------------------------------------------

@dp.table(
    name="sales_quarantine",
    comment="Sales records rejected by business validation rules"
)
def sales_quarantine():

    df = prepare_sales(
        spark.readStream.table("sales_bronze")
    )

    return (
        df
        .filter(~validate_sales(df))
        .withColumn(
            "_quarantine_reason",
            when(
                col("sale_id").isNull(),
                "Missing sale_id"
            ).otherwise("One or more business rules failed")
        )
    )


# --------------------------------------------------
# GOLD: Business-level Sales aggregations
# --------------------------------------------------

@dp.materialized_view(
    name="sales_gold",
    comment="Sales metrics aggregated by product, city and category"
)
def sales_gold():

    return (
        spark.read.table("sales_silver")
        .groupBy("product_name", "city", "category")
        .agg(
            count("sale_id").alias("total_orders"),
            spark_sum("quantity").alias("total_quantity"),
            round(spark_sum("total_amount"), 2).alias("total_revenue"),
            round(avg("total_amount"), 2).alias("average_order_value")
        )
    )
