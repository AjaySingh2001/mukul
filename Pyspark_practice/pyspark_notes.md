# PySPark

# Column Manipulation

### 1. What is a Column in PySpark?

In PySpark, you don’t work with Python lists or dicts.
You work with DataFrame + Column objects.

Example DataFrame:
```python
from pyspark.sql.types import *
from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("test").getOrCreate()
data = [
    ("Mukul", 25, "Indore", 55000),
    ("Rohan", 28, "Pune", 62000),
    ("Asha", 30, "Indore", 70000),
    ("Karan", 22, "Mumbai", 48000),
    ("Riya", 26, "Pune", None)
    ]

schema = StructType([
    StructField("Name", StringType()),
    StructField("Age", IntegerType()),
    StructField("City", StringType()),
    StructField("Salary", IntegerType()),
    # StructField("Temp", IntegerType()),
])

df = spark.createDataFrame(data, schema)
# Type-2 

data = [
    (1, "Mukul", 50000),
    (2, "Rahul", 60000),
    (3, "Sneha", 55000)
]

df = spark.createDataFrame(data, ["id", "name", "salary"])

```
- id, name, salary → columns
- Each column has a type, value, and operations

### 2. How to SELECT Columns
```python
✔ Select 1 column
df.select("name").show()

✔ Select multiple
df.select("id", "name").show()

✔ Using col()
from pyspark.sql.functions import col

df.select(col("salary")).show()

```
> ➡️ Why col()?
> Because when you want to apply functions (upper, lower, cast), you need Column object.

### 3. Add a New Column
```python
✔ Add new derived column
df = df.withColumn("bonus", col("salary") * 0.10)

✔ Add constant column
from pyspark.sql.functions import lit

df = df.withColumn("country", lit("India"))

```
> ➡️ lit() means adding a literal (fixed) value.

### 4. Rename Column
```python
✔ Simple rename
df = df.withColumnRenamed("salary", "emp_salary")

✔ Rename using alias
df = df.select(col("name").alias("employee_name"))
```

### 5. Drop Column
```python
df = df.drop("country")
df = df.drop("bonus", "id")
```

### 6. Convert / Change Column Data Type
```python
✔ Use cast
df = df.withColumn("salary", col("salary").cast("float"))
```
> Types can be: "int", "float", "string", "date"

### 7. String Column Manipulation
```python
✔ Uppercase / lowercase
df = df.withColumn("name_upper", upper(col("name")))

✔ substring
df = df.withColumn("short", col("name").substr(1, 3))

✔ contains
df.filter(col("name").contains("a")).show()

✔ regex replace
df = df.withColumn("clean", regexp_replace("name", "a", "A"))
```
### 8. Mathematical Operations
```python
df = df.withColumn("double_salary", col("salary") * 2)
df = df.withColumn("salary_plus_5000", col("salary") + 5000)
df = df.withColumn("tax", col("salary") * 0.06)
```

### 9. Conditional Column (IF / ELSE)

Use when + otherwise:
```python
df = df.withColumn(
    "grade",
    when(col("salary") > 55000, "High").otherwise("Medium")
)
```
### 10. Handle Null Values

```python
✔ Fill null
df = df.fillna({"name": "unknown", "salary": 0})

✔ Drop null row
df = df.na.drop()

✔ Replace values
df = df.na.replace({"Rahul": "Rahu"})
```

### 11. Date Column Operations
```python
# Convert string → date:

df = df.withColumn("join_date", to_date("join_date"))

# Extract year/month/day:

df = df.withColumn("year", year("join_date"))
df = df.withColumn("month", month("join_date"))
df = df.withColumn("day", dayofmonth("join_date"))


# Add months:

df = df.withColumn("next_month", add_months("join_date", 1))
```

### 12. Combine Columns
```python
✔ concat
df = df.withColumn("full_info", concat(col("name"), lit("_"), col("salary")))

✔ concat_ws (delimiter)
df = df.withColumn("info", concat_ws("|", "id", "name", "salary"))
```

### 13. Window Functions (VERY IMPORTANT)
```python
from pyspark.sql.window import Window

w = Window.orderBy("salary")

✔ Rank
df = df.withColumn("rnk", rank().over(w))

✔ Row number
df = df.withColumn("rn", row_number().over(w))

✔ Running total
df = df.withColumn("running_total", sum("salary").over(w))
```

### 14. Remove Duplicate Rows

Based on 1 column:
```python
df = df.dropDuplicates(["name"])

On all columns:

df = df.dropDuplicates()
```
### 15. Reorder Columns
```python
df = df.select("name", "salary", "id")
```


# Row Manipulation

### 1. Filter Rows (MOST IMPORTANT)
```python
# ✔ Keep rows based on condition
df.filter(col("salary") > 55000).show()

# ✔ Multiple conditions (&, |)
df.filter((col("salary") > 55000) & (col("name") == "Rahul")).show()

# ✔ Use == , != , > , >=
df.filter(col("name") != "Mukul").show()
```
### 2. Drop Duplicate Rows
```python
# ✔ Drop duplicates from whole rows
df.dropDuplicates().show()

# ✔ Drop duplicates based on specific column
df.dropDuplicates(["name"]).show()
```
### 3. Sort Rows
```python
# ✔ Ascending order
df.orderBy("salary").show()

# ✔ Descending
df.orderBy(col("salary").desc()).show()
```
### 4. Limit Rows (Head / Tail)
```python
# ✔ Limit first N rows
df.limit(2).show()

# ✔ First row (like df.head())
df.first()

# ✔ Collect all data to Python list
df.collect()
```
### 5. Replace Values in Rows
```python
# ✔ Replace inside column
df = df.na.replace({"Mukul": "MK"})

# ✔ Replace multiple values
df = df.replace(["Mukul", "Rahul"], ["MK", "RL"], "name")
```

### 6. Remove Rows
```python
# ✔ Remove rows with nulls
df.na.drop().show()
# ✔ Drop rows where ANY column is null
df.na.drop(how="any").show()
# ✔ Drop rows where ALL columns are null
df.na.drop(how="all").show()
# ✔ Drop rows where specific columns are null
df.na.drop(subset=["salary"]).show()
```

### 7. Fill Missing Values
```python
df.fillna({"salary": 0, "name": "unknown"}).show()
```

### 8. Sample Rows (Random Sampling)
```python
# ✔ Sample 50% rows
df.sample(0.5).show()

# ✔ Sample with or without replacement
df.sample(withReplacement=True, fraction=0.4).show()

# ✔ Sample fixed number of rows
df.sampleBy("name", {"Mukul": 1.0, "Rahul": 0.5})
```
### 9. Add New Rows to DataFrame

PySpark DF is immutable → you cannot append row directly.
But you can union a new row:
```python
✔ Add one row
from pyspark.sql import Row

new_row = spark.createDataFrame([Row(id=4, name="Amit", salary=65000)])
df = df.union(new_row)

# ✔ Add multiple rows
new_data = [(5, "Tina", 70000), (6, "Karan", 80000)]
new_df = spark.createDataFrame(new_data, ["id", "name", "salary"])

df = df.union(new_df)
```
### 10. Conditional Row Filtering (Case When for Rows)
```python
# ✔ Keep only employees with salary > 55000
df.where(col("salary") > 55000).show()
# ✔ Keep only names that start with 'M'
df.filter(col("name").startswith("M")).show()
# ✔ Contains
df.filter(col("name").contains("a")).show()
```

### 11. Distinct Rows
```python
df.distinct().show()
```

### 12. Row Aggregation (counts, sums, etc.)
```python
df.count()               # number of rows
df.agg(sum("salary")).show()
df.groupBy("name").count().show()
```

### 13. Window Operations on Rows (Row Based Windows)

Used for:

Running totals

Previous / next row

Rank / row_number

Example:
```python
from pyspark.sql.window import Window

w = Window.orderBy("salary")
df = df.withColumn("prev_salary", lag("salary", 1).over(w))
df = df.withColumn("next_salary", lead("salary", 1).over(w))
```
