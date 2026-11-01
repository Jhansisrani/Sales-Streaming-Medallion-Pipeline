from pyspark import pipelines as dp
from pyspark.sql.functions import (
    sum, count, avg, current_timestamp
)


@dp.materialized_view(
    name="sales_gold",
    comment="Aggregated sales metrics by product, category and city"
)
def sales_gold():

    return (
        spark.read.table("sales_silver")
        .groupBy("product_name", "category", "city")
        .agg(
            count("sale_id").alias("total_sales"),
            sum("quantity").alias("total_quantity"),
            sum("total_amount").alias("total_revenue"),
            avg("total_amount").alias("average_sale_amount")
        )
        .withColumn("_updated_at", current_timestamp())
    )