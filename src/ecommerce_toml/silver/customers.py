from pyspark import pipelines as dp
from pyspark.sql.functions import col


catalog = spark.conf.get("ecommerce.catalog")
schema = spark.conf.get("ecommerce.silver.schema")
bronze_schema = spark.conf.get("ecommerce.bronze.schema")

@dp.materialized_view(name=f"{catalog}.{schema}.customers")
def silver_customers():

    return (
        spark.read.table(f"{catalog}.{bronze_schema}.customers_stream")
        .dropDuplicates(["customer_id"])
        .filter(col("customer_id").isNotNull())
    )