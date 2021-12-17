import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy


def difference(dataset, interval=1):
    diff = list()
    for i in range(interval, len(dataset)):
        value = dataset[i] - dataset[i - interval]
        diff.append(value)
    return diff


df = pd.read_excel('Tables/разводы (1).xlsx', index_col='time')
d = {'time': df.index[1:]}
for i in df:
    if i != 'time':
        d[i] = df[i][1:]
        if df[i][0] > 0:
            d[i] = difference(df[i])
df_1 = pd.DataFrame(d)
df_1.to_excel('Tables/чистые разводы.xlsx', index=False)
