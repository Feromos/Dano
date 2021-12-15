import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy


def med(a):
    k = len(a)
    if k % 2 == 0:
        return (a[k // 2] + a[k // 2 + 1]) // 2
    else:
        return a[k // 2 + 1]


df_1 = pd.read_excel('Tables/разводы.xlsx', index_col='time')
df_2 = pd.read_excel('Tables/корзины за зарплату.xlsx', index_col='time')
df_3 = pd.read_excel('Tables/безработица.xlsx', index_col='time')
d = {'': ['разводы', 'корзины за зарплату', 'безработица']}
for i in df_2:
    d[i] = [med(df_1[i]), med(df_2[i]), med(df_3[i])]
df_3 = pd.DataFrame(d)
df_3.to_excel('Tables/медианные значения.xlsx', index=False)
