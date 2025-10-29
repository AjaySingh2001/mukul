import pandas as pd 

df = pd.read_csv('Sample.csv')

# data = {
#     'Cars':["Audi","Mercedez","Toyota"],
#     'Passings':[2,4,8]
# }

# df = pd.DataFrame(data)

# l = {"day1":200, "day2":300, "day3": 400}
# s = pd.Series(l,index=["day1","day2"])

x = df["Calories"].mean()

df["Date"] = pd.to_datetime(df['Date'], format='mixed')

df.loc[1,"Calories"] = 5.00

# print(df.to_string())

df.drop_duplicates(inplace=True)

print(df.to_string())