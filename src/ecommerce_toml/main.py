from pyspark.sql import SparkSession
from ecommerce_toml.config import load_config


def main():
    config = load_config()

    spark = (
        SparkSession.builder
        .appName(config["spark"]["app_name"])
        .master(config["spark"]["master"])
        .getOrCreate()
    )

    try:
        print(f"Environment: {config['app']['environment']}")

        # Your Spark transformations go here.

    finally:
        spark.stop()


if __name__ == "__main__":
    main()