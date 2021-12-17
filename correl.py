import csv
import pandas as pd
import matplotlib.pyplot as plt
from numpy import log
import numpy

df_1 = pd.read_excel('Tables/корреляция.xlsx')
df_2 = pd.read_excel('Tables/корзины за зарплату.xlsx', index_col='time')
d1 = {'region': df_2.columns, 'values': []}
d2 = {'region': df_2.columns, 'values': []}
for i in df_2:
    if i != 'time':
        d1['values'].append(df_1[i][0])
        d2['values'].append(sum(df_2[i][1:49]) / 48)
df_3 = pd.DataFrame(d1)
df_4 = pd.DataFrame(d2)
print(df_3['values'].corr(df_4['values']))
# df_5 = pd.DataFrame(d)
# df_5.to_excel('Tables/корреляция.xlsx', index=False)
