
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum

def main():
    spark = (
        SparkSession.builder
        .appName("ecommerce-cluster-test")
        .getOrCreate()
    )

    print(f"Spark master: {spark.sparkContext.master}")
    print(f"Spark version: {spark.version}")

    # Generate 1 million rows distributed across the cluster
    df = spark.range(1_000)

    result = (
        df.withColumn("amount", col("id") % 100)
        .groupBy()
        .agg(spark_sum("amount").alias("total_amount"))
    )

    result.show()

    spark.stop()

if __name__ == "__main__":
    main()
