from pyspark.sql import SparkSession


def create_spark(config):

    app_name = config.get(
        "spark",
        "app_name"
    )

    master = config.get(
        "spark",
        "master"
    )
    builder = (
        SparkSession.builder
        .appName(app_name)
        .master(master)
        .config("spark.sql.adaptive.enabled", "false")
        .config("spark.sql.autoBroadcastJoinThreshold", -1)
        .config("spark.sql.adaptive.coalescePartitions.enabled", "false")
    )
    
    return builder.getOrCreate()