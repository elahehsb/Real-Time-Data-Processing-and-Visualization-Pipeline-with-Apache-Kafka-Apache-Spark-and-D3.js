from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

spark = SparkSession.builder \
    .appName("RealTimeDataProcessing") \
    .getOrCreate()

schema = StructType([
    StructField("timestamp", DoubleType(), True),
    StructField("value", DoubleType(), True)
])

df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "real-time-data") \
    .load()

df = df.selectExpr("CAST(value AS STRING)")

json_df = df.select(from_json(col("value"), schema).alias("data")).select("data.*")

query = json_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
