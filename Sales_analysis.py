import pandas as pd
data = pd.read_csv("train.csv")
print(data.head())
print(data.describe())
region_sales = data.groupby("Region")["Sales"].sum()
print(region_sales)