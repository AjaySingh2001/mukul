import pandas as pd
import os
import pyexcel as p
import json
from datetime import datetime, date

import zipfile
from io import BytesIO


# method1
# data = pd.read_excel('/home/developer/Mukul/Pandas/monitoring_data.ods', engine='odf')

# Method2 (Worked)
# make three csv files by excel sheets and then merge it.
# excel = pd.ExcelFile("/home/developer/Mukul/Pandas/pandas_practice/monitoring_data_new.xlsx")
# df = pd.read_excel(excel, sheet_name=excel.sheet_names[0])
# df.to_csv("large_file.csv", index = False)
# data = pd.read_csv('/home/developer/Mukul/large_file.csv')
# df = pd.DataFrame(data)
# print(df.to_string())

# Method3
# excel = pd.ExcelFile("/home/developer/Mukul/Pandas/monitoring_data.ods", engine="odf")
# data = pd.read_excel("/home/developer/Mukul/Pandas/monitoring_data.ods", engine='odf')
# os.rename("/home/developer/Mukul/Pandas/monitoring_data.ods", "/home/developer/Mukul/Pandas/monitoring_data.xlsx")
# print("File renamed successfully")
# excel = pd.ExcelFile("/home/developer/Mukul/Pandas/monitoring_data.xlsx")
# df = pd.read_excel(excel, sheet_name=excel.sheet_names[0])
# # print(excel)
# df.to_csv("/home/developer/Mukul/Pandas/temp.csv", index = False)
# data = pd.read_csv('/home/developer/Mukul/Pandas/temp.csv')
# df = pd.DataFrame(data)
# print(df.head(5))


# Method4 (Worked)
    
# p.save_book_as(
#     file_name="/home/developer/Mukul/Pandas/monitoring_data.ods",
#     dest_file_name="/home/developer/Mukul/Pandas/monitoring_data.csv"
# )

# d1 = pd.read_csv('Pandas/monitoring_data__Abstraction-Discharge__2.csv')
# d2 = pd.read_csv('Pandas/monitoring_data__Groundwater_Level__0.csv')
# d3 = pd.read_csv('Pandas/monitoring_data__Groundwater_Quality__1.csv')

# df_list =[]
# for i in [d1,d2,d3]:
#     df_list.append(pd.DataFrame(i))

# new_df = pd.concat(df_list, ignore_index=True)

# print("json converting start...")
# new_df.to_json("Pandas/record.json", indent=4)
# print("json converting done...")


# Method5 (Worked(Best)- Low Ram Optimized)

# temp = p.get_book(file_name = "/home/developer/Mukul/Pandas/monitoring_data.ods")
# data_dict = temp.to_dict()

# def default_converter(o):
#     if isinstance(o, (datetime, date)):
#         return o.isoformat()  
#     raise TypeError(f"Type {o} not serializable")

# with open("/home/developer/Mukul/Pandas/monitoring_data.json", "w") as f:
#     json.dump(data_dict, f, indent=4, default=default_converter)
# print("Process Successfully Done!!")

# Method6
# zip_path = "/home/developer/Mukul/Pandas/monitoring_data.zip"

# with zipfile.ZipFile(zip_path, 'r') as z:
#     # List the contents
#     print("Getting data done.")

#     # Assume the first file is your .ods
#     ods_name = z.namelist()[0]
#     print("Getting data done1.")

#     # # Read that file into memory (without extracting)
#     with z.open(ods_name) as ods_file:
#         data = ods_file.read()
#         print("Getting data done.2")
        
# # Now read it using pandas (ODS engine)
# df = pd.read_excel(BytesIO(data), engine="odf")
# print("Getting data done3.")

zip_path = "/home/developer/Mukul/Pandas/monitoring_data.zip"

with zipfile.ZipFile(zip_path) as z:
    ods_name = z.namelist()[0]
    with z.open(ods_name) as f:
        df = pd.read_excel(f, engine='odf')

print("Process Done...")
