from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("Import file").getOrCreate()

df = spark.read.csv("Pyspark_practice/events.csv", header=True)

data = [
    ()
]

df.printSchema()

