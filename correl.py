import csv
import pandas as pd
import matplotlib.pyplot as plt
from numpy import log
import numpy

df_1 = pd.read_excel('Tables/разводы.xlsx', index_col='time')
df_2 = pd.read_excel('Tables/корзины за зарплату.xlsx', index_col='time')
d = {}
for i in df_1:
    if i != 'time':
        d[i] = df_1[i].corr(df_2[i])
df_5 = pd.DataFrame(d)
df_5.to_excel('Tables/корреляция.xlsx', index=False)
