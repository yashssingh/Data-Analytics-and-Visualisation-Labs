# %%
# YASH KUMAR SINGH
# 202151181

import pandas as pd
import json
import csv

# %%
df = pd.read_csv('primary_completion_rate_female.csv', skiprows=4, usecols=range(67))

# %%
df['average_rate'] = df.mean(axis=1)
print(df['average_rate'])
df.to_csv('primary_completion_rate_female_with_average.csv', index=False)


# %%
population_df = pd.read_csv("population_of_female.csv", skiprows=4, usecols=range(67))
population_df['Latest Population'] = population_df.loc[:, '1960':'2021'].iloc[:, -1]
print(population_df['Latest Population'])
df.to_csv('population_of_female_with_latest_population', index=False)


# %%
weighted_average = ((df['average_rate'] * population_df['Latest Population']) / population_df['Latest Population'].sum()).sum()
print(f"\nWeighted average of 'average_rate': {weighted_average}")

# %%
median_completion_rate = df['average_rate'].median()
print(f"Median of 'average_rate': {median_completion_rate}")

# %%
iqr = df['average_rate'].quantile(0.75) - df['average_rate'].quantile(0.25)
print(f"Interquartile Range (IQR) of 'average_rate': {iqr}")


# %%
variance = df['average_rate'].var()
print(f"Variance of 'average_rate': {variance}")


