from pyspark import pipelines as dp

catalog = spark.conf.get("ecommerce.catalog")
schema = spark.conf.get("ecommerce.bronze.schema")
raw_path = spark.conf.get("ecommerce.raw_path")
products_path = f"{raw_path}/products"
@dp.table(name=f"{catalog}.{schema}.products_stream")
def bronze_products_stream():
    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("header", "true")
        .load(products_path)
    )