# # Series
import pandas as pd

arr = [1,2,3]
# # ser = pd.Series(arr)
# ser = pd.Series([1,2,3,4])
# print(ser)

# lables

# ser = pd.Series(arr, index=['x','y','z'])
# print(ser)

# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories)

# print(myvar)

# Dataframe

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# myvar = pd.DataFrame(data, index = ["day1", "day2", "day3"])

# print(myvar)

# data = pd.read_json('/home/developer/Mukul/Pandas/data.json')

# df = pd.DataFrame(data)
# print(df.to_string())


df = pd.read_csv('/home/developer/Mukul/Pandas/data.csv')

# mn = df["Calories"].mean()
# mdn = df["Calories"].median()
# md = df["Calories"].mode()[0]
# print(mn, mdn, md)
# df.fillna({"Calories":10000}, inplace=True)
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df.to_string())
