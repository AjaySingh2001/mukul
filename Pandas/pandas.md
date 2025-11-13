# Pandas
Pandas is a Python library used for working with data sets.
It has functions for analyzing, cleaning, exploring, and manipulating data.

### Why use pandas?
Pandas allows us to analyze big data and make conclusions based on statistical theories.
Pandas can clean messy data sets, and make them readable and relevant.
Relevant data is very important in data science.

### What pandas can do?
Is there a correlation between two or more columns?
- What is average value?
- Max value?
- Min value?

Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. This is called cleaning the data.

> The source code for Pandas is located at this github repository https://github.com/pandas-dev/pandas

### import Pandas as pd
Pandas is usually imported under the pd alias.
```python
import pandas as pd
```
### Checking Pandas Version
The version string is stored under __version__ attribute.
```python
import pandas as pd

print(pd.__version__)
```

### Pandas Series
A Pandas Series is like a column in a table.
It is a one-dimensional array holding data of any type.
```python
import pandas as pd

arr = [1,2,3,4]
# ser = pd.Series(arr)
ser = pd.Series([1,2,3,4])
print(ser)
```
### Labels
If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
This label can be used to access a specified value.
```python
#Return the first value of the Series:
print(myvar[0])
```
### Create Labels
With the index argument, you can name your own labels.
```python
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
```
### Key/Value Objects as Series
You can also use a key/value object, like a dictionary, when creating a Series.
```python
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)
```
Create a Series using only data from "day1" and "day2":
```python
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
```

### DataFrames
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
Series is like a column, a DataFrame is the whole table.

Create a DataFrame from two Series:
```python
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)
```python
### Locate Row
As you can see from the result above, the DataFrame is like a table with rows and columns.
Pandas use the loc attribute to return one or more specified row(s)
```python
print(df.loc[0])
#use a list of indexes:
print(df.loc[[0, 1]])
```

### Named Indexes
With the index argument, you can name your own indexes.
```python
#Add a list of names to give each row a name:
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df) 
```

### Load Files Into a DataFrame
If your data sets are stored in a file, Pandas can load them into a DataFrame.
```python
import pandas as pd

df = pd.read_csv('data.csv')

print(df) 
```
A simple way to store big data sets is to use CSV files (comma separated files).
CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
>Note : If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
```python
import pandas as pd

df = pd.read_csv('data.csv')

print(df) # print 5 top rows and 5down rows
print(df.to_string()) # print all rows.
```

### max_rows
The number of rows returned is defined in Pandas option settings.
You can check your system's maximum rows with the pd.options.display.max_rows statement.
```python
print(pd.options.display.max_rows)
```
```python
# Increase the maximum number of rows to display the entire DataFrame:
import pandas as pd
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df) 
```

### Read JSON
Big data sets are often stored, or extracted as JSON.
JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.
In our examples we will be using a JSON file called 'data.json'.
```python 
#Similar to CSV file
#Load the JSON file into a DataFrame:

import pandas as pd

df = pd.read_json('data.json')

print(df.to_string()) 
```
> Note: If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:
```python
import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 
```
### Viewing the Data
One of the most used method for getting a quick overview of the DataFrame, is the head() method.
The head() method returns the headers and a specified number of rows, starting from the top.
```python
# Get a quick overview by printing the first 10 rows of the DataFrame:

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))
```
There is also a tail() method for viewing the last rows of the DataFrame.
The tail() method returns the headers and a specified number of rows, starting from the bottom.
```python
# Get a quick overview by printing the last 5 rows of the DataFrame:

print(df.tail()) 
```
### Info About the Data
The DataFrames object has a method called info(), that gives you more information about the data set.
```python
# Print information about the data:

print(df.info()) 
```


# Pandas - Cleaning Data
Data cleaning means fixing bad data in your data set.

Bad data could be:
* Empty cells
* Data in wrong format
* Wrong data
* Duplicates

### Pandas - Cleaning Empty Cells
Empty cells can potentially give you a wrong result when you analyze data.

### Remove Rows
One way to deal with empty cells is to remove rows that contain empty cells.
This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
```python
# Return a new Data Frame with no empty cells:

import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())
```
>Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

If you want to change the original DataFrame, use the inplace = True argument:
```python
# Remove all rows with NULL values:

import pandas as pd

df = pd.read_csv('data.csv')

df.dropna(inplace = True)

print(df.to_string())
```

### Replace Empty Values
Another way of dealing with empty cells is to insert a new value instead.
This way you do not have to delete entire rows just because of some empty cells.
The fillna() method allows us to replace empty cells with a value:
```python
# Replace NULL values with the number 130:

import pandas as pd

df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)
```

### Replace Only For Specified Columns
The example above replaces all empty cells in the whole Data Frame.
To only replace empty values for one column, specify the column name for the DataFrame:
```python
# Replace NULL values in the "Calories" columns with the number 130:

import pandas as pd

df = pd.read_csv('data.csv')

df.fillna({"Calories": 130}, inplace=True)
```
### Replace Using Mean, Median, or Mode
A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:
```python
Calculate the MEAN, and replace any empty values with it:

import pandas as pd

df = pd.read_csv('data.csv')

mn = df["Calories"].mean()
mdn = df["Calories"].median()
md = df["Calories"].mode()[0]

df.fillna({"Calories": mn}, inplace=True)
```

## Pandas - Cleaning Data of Wrong Format
Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.
Pandas has a to_datetime() method for this:
```python
# Convert to date:

import pandas as pd

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())
```

### Removing Rows
The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, and we can remove the row by using the dropna() method.
```python
df.dropna(subset=['Date'], inplace=True)
```

### Pandas Fixing wrong data
* "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".
* Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.
* If you take a look at our data set, you can see that in row 7, the duration is 450, but for all the other rows the duration is between 30 and 60.
* It doesn't have to be wrong, but taking in consideration that this is the data set of someone's workout sessions, we conclude with the fact that this person did not work out in 450 minutes.

How can we fix wrong values, like the one for "Duration" in row 7?
### Replacing Values
One way to fix wrong values is to replace them with something else.
In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7:
```python
# Set "Duration" = 45 in row 7:

df.loc[7, 'Duration'] = 45
```
For small data sets you might be able to replace the wrong data one by one, but not for big data sets.
To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.
```python
# Loop through all values in the "Duration" column.
# If the value is higher than 120, set it to 120:

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
```
### Removing Rows
Another way of handling wrong data is to remove the rows that contains wrong data.
This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.
```python

for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.dropna(x, inplace=True)
```

## Pandas - Removing Duplicates
Duplicate rows are rows that have been registered more than one time.
### Discovering Duplicates
To discover duplicates, we can use the duplicated() method.
The duplicated() method returns a Boolean values for each row:
```python
# Returns True for every row that is a duplicate, otherwise False:
print(df.duplicated())
```

### Removing Duplicates
To remove duplicates, use the drop_duplicates() method.
```python
df.drop_duplicates(inplace=True)
```
>Note: The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.

## Pandas Data- Co-relations
### Finding Relationships
A great aspect of the Pandas module is the corr() method.
The corr() method calculates the relationship between each column in your data set.
The examples in this page uses a CSV file called: 'data.csv'.
```python
# Show the relationship between the columns:
df.corr()
```

### Joins in Pandas
Joins allow you to combine two DataFrames based on a common column (key).
In pandas, joins are performed using: 
```python
pd.merge()
# or
df1.merge(df2)
```
### Types of Joins in Pandas (Same as SQL)
| Join Type                  | Meaning                                    | Keeps rows from |
| -------------------------- | ------------------------------------------ | --------------- |
| **INNER JOIN**             | Only matching rows                         | Both tables     |
| **LEFT JOIN**              | All rows from left, matched from right     | Left            |
| **RIGHT JOIN**             | All rows from right, matched from left     | Right           |
| **OUTER JOIN / FULL JOIN** | All rows from both, unmatched rows get NaN | Both            |

* INNER JOIN (Common records only)
  * pd.merge(df1.df2, on='id', how='inner')

* LEFT JOIN (All rows from left DataFrame)
  * pd.merge(df1.df2, on='id', how='left')

* RIGHT JOIN (All rows from right DataFrame)
  * pd.merge(df1.df2, on='id', how='right')

* FULL OUTER JOIN (All rows, unmatched as NaN)
  * pd.merge(df1.df2, on='id', how='outer')