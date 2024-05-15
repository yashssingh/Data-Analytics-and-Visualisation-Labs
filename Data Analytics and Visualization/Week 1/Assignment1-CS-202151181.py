# %%
import pandas as pd
import json
import sys

# %%
# Q1. 1. Create two data frames by reading above two files. 

# CSV FILE READING AND DATAFRAME CREATION
csv_file_path = '/Users/yashsingh/Desktop/Data Analytics and Visualization/Week 1/district_level_service_msme.csv'

# Creating dataframes from the files
service_df = pd.read_csv(csv_file_path)

# Displaying the dataframes
print("\nService MSME Dataframe:")
print(service_df)

# %%
# JSON FILE READING AND DATAFRAME CREATION
filepath="/Users/yashsingh/Desktop/Data Analytics and Visualization/Week 1/district_level_manufacturing_msme.json"
f = open(filepath)
data=json.load(f)
#data=pd.read_json(filepath)

#df=pd.DataFrame(data) # this return an error

print(data)
#print(data.keys())
print(data["fields"])
print(data["data"])

# Create data frame
df=pd.DataFrame(data["data"])
print(df)

# Assign  names to columns
clmns=[dic["label"] for dic in data["fields"]]
print(clmns)
df=pd.DataFrame(data["data"],columns=clmns)
print(df)

# %%


# Q2. Find out total ”Small” Manufacturing MSME in India. 

df['SMALL']=pd.to_numeric(df['SMALL'])
column_sum =  (df['SMALL'].sum())
column_sum


# %%


# Q3. Create a dataframe having a state wise total number of ”Micro”,”Small” and ”Medium” Services MSE (as shown below) and save the results as a CSV file. 

# Read the CSV file
service_df = pd.read_csv('/Users/yashsingh/Desktop/Data Analytics and Visualization/Week 1/district_level_service_msme.csv')

# Group by state and sum the counts for each category
df_1 = service_df.groupby("STATE_NAME").sum()["MICRO"]
df_2 = service_df.groupby("STATE_NAME").sum()["SMALL"]
df_3 = service_df.groupby("STATE_NAME").sum()["MEDIUM"]

# Save the results as a CSV file
df_f = pd.merge(df_1, df_2, on="STATE_NAME")
df_f1 = pd.merge(df_f, df_3, on="STATE_NAME")
df_f1.to_csv("MSM.csv")
print(df_f1)
print()


# %%


# Q4. Join the both the data frame based on common STATE NAME, DISTRICT NAME, Lg Dist Code and Last Updated. The result should look like below. ”x” and ”y” in the image below represent the manufacturing MSME and service MSME respectively.

filepath="/Users/yashsingh/Desktop/Data Analytics and Visualization/Week 1/district_level_manufacturing_msme.json"
f = open(filepath)
data=json.load(f)
columns=pd.DataFrame(data["fields"])["label"].tolist()
df=pd.DataFrame(data["data"],columns=columns)
final = pd.merge(df,service_df,on='STATE_NAME')
final.to_csv("Final_merge.csv")
print(final)

# %%


# Q5. Create a Pivot Table having rows STATE NAME and columns Service and Manufacturing ”MSME” as shown below. Use ”Sum” to add up district wise numbers. 
final["MICRO_x"]= final["MICRO_x"].astype(int)
final["SMALL_x"]= final["SMALL_x"].astype(int)
final["MEDIUM_x"]= final["MEDIUM_x"].astype(int)
pivot_table = pd.pivot_table(final,
                                values=["MICRO_x", "MICRO_y", "SMALL_x", "SMALL_y", "MEDIUM_x", "MEDIUM_y"],
                                index=["STATE_NAME"],
                                aggfunc={"MICRO_x": "sum", "MICRO_y": "sum",
                                "SMALL_x": "sum", "SMALL_y": "sum",
                                "MEDIUM_x": "sum", "MEDIUM_y": "sum"},
                                fill_value=0)

pivot_table.to_csv("pivot.csv")
print(pivot_table)


