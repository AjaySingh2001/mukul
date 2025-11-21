from pyspark.sql.functions import col, lit, upper, lower,when, concat_ws,lag,lead
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import Row
from pyspark.sql.window import Window
spark = SparkSession.builder.appName("test2").getOrCreate()

data = [
    (1, "Mukul", 50000),
    (2, "Rahul", 60000),
    (3, "Sneha", 55000)
]

df = spark.createDataFrame(data, ["id", "Name", "Salary"])

# df = df.withColumn("New_added", lit(None).cast(StringType()))
df = df.withColumn("Updated_Sal", col("Salary")*0.10)

# df.printSchema()
df = df.withColumnRenamed("Salary", "Emp_Salary")
# df = df.select(col("Name").alias("Emp_Name"))

# df = df.drop("Updated_Sal")
# df = df.withColumn("Emp_Salary", col("Emp_Salary").cast("float"))
# df.printSchema()

df = df.withColumn("Name", lower(col("Name")))

# new_df = df.withColumn("New_salary", when(col("Emp_Salary") > 50000, "High").otherwise((when(col("Emp_Salary") == 50000, "best")).otherwise("lower")))

# df = df.na.replace({"Mukul": "MUKUL"})

# df = df.withColumn("full_info", concat(col("Name"), lit("_"), col("Emp_Salary")))
# df = df.withColumn("info", concat_ws("|", "id", "Name", "Emp_Salary"))


# Row Manipulation

# row = df.filter((col("Emp_Salary") > 50000) & (col("Name") == "sneha"))

# row = df.filter(col("Name") != "mukul")

# row = df.orderBy("Emp_Salary")
# row = df.orderBy(col("Emp_Salary").desc())

# row = df.limit(10)
# row = df.first()
# row = df.collect()

# row = df.replace(["Deepak","rahul"], ["Mukul", "Ravi"], "Name")

# row = df.na.drop()
# row = df.na.drop(how="any")

# row = df.replace({50000:None})
# row = row.fillna({"Emp_Salary": 0})
# row = row.na.drop(subset=["Updated_Sal"])

# row = df.sample(0.5)
# row = df.sample(withReplacement=True, fraction=0.7)

# row = spark.createDataFrame([Row(id=4, Name="kapil", Emp_Salary=40000, Updated_Sal=10000)])
rows = spark.createDataFrame([(5, "Amit", 60000, 20000),(3, "Jayesh", 50000, 36000)], ["id","Name", "Salary", "Updated"])
df = df.union(rows)

# df = df.where(col("Emp_Salary") > 50000)
# df = df.filter(col("Name").startswith('A'))
# df = df.filter(col("Name").contains('m'))
df = df.distinct()

# print(df.count())
# df.agg(sum("Emp_Salary"))
df = df.withColumn("Emp_Salary",col("Emp_Salary").cast(IntegerType()))

# df.printSchema()
# total = df.sum("Emp_Salary"))
# df.groupBy("Emp_Salary").count().show()

w = Window.orderBy("Emp_Salary")

# df = df.withColumn("Prev_Salary", lag("Emp_Salary").over(w))
# df = df.withColumn("Prev_Salary", lead("Emp_Salary").over(w))
df.show()
# df.show()
# print(type(row), row)
