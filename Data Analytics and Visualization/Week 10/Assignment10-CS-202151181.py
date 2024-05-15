# %%
# YASH KUMAR SINGH
# 202151181
import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt


# Load the Cookie Cats data from CSV file
data = pd.read_csv('/Users/yashsingh/Desktop/Data Analytics and Visualization/Week 10/cookie_cats.csv')

# QUESTION 1 - Perform t-test for sum_gamerounds, retention_1, and retention_7
# Separate the data into two groups based on the 'version' column: gate_30 and gate_40
gate_30 = data[data['version'] == 'gate_30']
gate_40 = data[data['version'] == 'gate_40']

# Perform t-test for sum_gamerounds
t_stat_sum_gamerounds, p_value_sum_gamerounds = stats.ttest_ind(gate_30['sum_gamerounds'].dropna(), gate_40['sum_gamerounds'].dropna(), equal_var=False)

print("For sum_gamerounds:")
print(f"t-statistic: {t_stat_sum_gamerounds}")
print(f"p-value: {p_value_sum_gamerounds}")

alpha = 0.05
if p_value_sum_gamerounds < alpha:
    print("Reject the null hypothesis. There is a significant difference in the average number of game rounds between gate_30 and gate_40.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in the average number of game rounds between gate_30 and gate_40.")

# Perform t-test for retention_1
t_stat_retention_1, p_value_retention_1 = stats.ttest_ind(gate_30['retention_1'].astype(int), gate_40['retention_1'].astype(int), equal_var=False)

print("\nFor retention_1:")
print(f"t-statistic: {t_stat_retention_1}")
print(f"p-value: {p_value_retention_1}")

if p_value_retention_1 < alpha:
    print("Reject the null hypothesis. There is a significant difference in retention_1 between gate_30 and gate_40.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in retention_1 between gate_30 and gate_40.")

# Perform t-test for retention_7
t_stat_retention_7, p_value_retention_7 = stats.ttest_ind(gate_30['retention_7'].astype(int), gate_40['retention_7'].astype(int), equal_var=False)

print("\nFor retention_7:")
print(f"t-statistic: {t_stat_retention_7}")
print(f"p-value: {p_value_retention_7}")

if p_value_retention_7 < alpha:
    print("Reject the null hypothesis. There is a significant difference in retention_7 between gate_30 and gate_40.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in retention_7 between gate_30 and gate_40.")


# %%

# Load the IPL ipl_data from CSV file
ipl_data = pd.read_csv('/Users/yashsingh/Desktop/Data Analytics and Visualization/Week 10/IPL_Auction_2022_FullList.csv')

# Create a contingency table for "Specialism" and "Batting"
contingency_table = pd.crosstab(ipl_data['Specialism'], ipl_data['Batting'])

print("Contingency Table:")
print(contingency_table)

# Perform Chi-square test
chi2_stat, p_value, dof, expected = stats.chi2_contingency(contingency_table)

print("\nChi-square Statistic:", chi2_stat)
print("p-value:", p_value)
print("Degrees of Freedom:", dof)
print("\nExpected Frequencies Table:")
print(expected)

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("\nReject the null hypothesis. There is a significant association between 'Specialism' and 'Batting' type of players.")
else:
    print("\nFail to reject the null hypothesis. There is no significant association between 'Specialism' and 'Batting' type of players.")

# Visualization
plt.figure(figsize=(10, 6))

# Plot the contingency table
sns.heatmap(contingency_table, annot=True, fmt="d", cmap="YlGnBu", cbar=True, square=True)
plt.title("Contingency Table: Specialism vs Batting")
plt.xlabel("Batting")
plt.ylabel("Specialism")
plt.show()

# Plot the expected frequencies table
plt.figure(figsize=(10, 6))

sns.heatmap(expected, annot=True, fmt=".2f", cmap="YlGnBu", cbar=True, square=True)
plt.title("Expected Frequencies Table")
plt.xlabel("Batting")
plt.ylabel("Specialism")
plt.show()



