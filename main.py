# %% Dependencies
import os
import pandas as pd
import sklearn as sk
import numpy as np
from sklearn.linear_model import LinearRegression
# %% Read data

data = pd.read_csv("diamonds-m.csv")
print(data.describe())
print(data.head(10))

# %% Crosstab b/w carat & cut

print(pd.crosstab(data["carat"], data["cut"]))

# %% Check for null entries
sel_list = ["cut","color","clarity","depth", "x", "y", "z"]
for field in sel_list:
    print("No. of empty entries for {}:\t".format(field), data[field].isnull().sum())

# %% Check for zero valued entries

print("\n")
for field in data.columns:
    print(
        "No. of zero valued entries for {}:\t".format(field),
        data[field].isin([0,'0']).sum(),
    )


##### Data Cleaning #####
# %% Converting zeros to Null

data_c = data.replace([0,'0'], np.nan)
# data_c = data
print("\n conversion of zeros to null is DONE!!!")

# %% converting outliers to Null
for field in data_c.columns:
        if field != 'id' and data_c[field].dtype != object:
                Q1 = data_c[field].quantile(q=0.25)
                Q3 = data_c[field].quantile(q=0.75)
                IQR = Q3 - Q1
                outlier_lower_limit = Q1 - (1.5 * IQR)
                outlier_upper_limit = Q3 + (1.5 * IQR)
                data_c.loc[data_c[field] < outlier_lower_limit, field] = np.nan
                data_c.loc[data_c[field] > outlier_upper_limit, field] = np.nan
print("\n conversion of outliers to null is DONE!!!")

# %% convert undefined to Null
for cat in ["cut","color","clarity"]:
        data_c.loc[data_c[cat] == "", cat] = np.nan
print("\n conversion of undefined to null is DONE!!!")

# %% Final tally of Null occurances
print("\n ####################### \n Final Tally of null occurances \n")
for field in data_c:
    print("No. of empty entries for {}:\t".format(field), data_c[field].isnull().sum())

# %% Write out csv to file

data_c.to_csv("output.csv", index=False)

# %% ways of printing one entry
print(data_c.head(1))
print(data_c[data_c.id == 1])

# %% Builduing Machine Learning model 1

ml_data = pd.read_csv("output.csv")
input_data = ml_data.drop("id","price")
model = LinearRegression()
