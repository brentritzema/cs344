# Little script to find the mean and sd of all the networks for a 25x run
import numpy as np
import pandas as pd

df = pd.DataFrame()

for i in range(1,26):
	results = pd.read_csv("run_results/result_{0}.csv".format(i))
	df = df.append(results["f1"]).rename({"f1": "f1_{0}".format(i)}, axis='index')

df.loc['mean'] = df.mean()
df.loc['std'] = df.std()
df['max'] = df.max(axis=1)
df['min'] = df.min(axis=1)
print(df)
