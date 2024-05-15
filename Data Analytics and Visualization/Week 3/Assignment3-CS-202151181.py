# %%
# YASH KUMAR SINGH 202151181

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from joypy import joyplot


# %%
data = pd.read_csv("/Users/yashsingh/Desktop/Data Analytics and Visualization/Week 3/grains_production_india_from_2001_to_2017.csv")

melted_data = pd.melt(data, id_vars=['Year'], var_name='Crop', value_name='Production')



# %%
# %%
plt.figure(figsize=(10,30))

# Violin plot
plt.subplot(3, 1, 1)
sns.violinplot(x='Production', y='Crop', data=melted_data)
plt.xticks(rotation=90)
plt.title('Violin Plot')

# %%
# Box plot
plt.subplot(3, 1, 2)
sns.boxplot(x='Crop', y='Production', data=melted_data)
plt.xticks(rotation=90)
plt.title('Box Plot')

# %%
# Strip plot
plt.subplot(3, 1, 3)
sns.stripplot(x='Crop', y='Production', data=melted_data, jitter=True, alpha=0.5)
plt.xticks(rotation=90)
plt.title('Strip Plot')

plt.tight_layout()
plt.show()


