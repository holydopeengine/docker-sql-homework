import sys

import pandas as pd 

month = ["January", "February", "March",]


df = pd.DataFrame({"day": [1, 2, 3], "num_passenger": [3, 4, 5], "luggages(kg)": [50, 60, 70]})
df['month'] = month
print(df.head())

df.to_parquet(f"output_{month}.parquet")

print(f"hello_pipeline {month}")

