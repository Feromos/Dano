import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy


def middle(a):
    a = sorted(a[:49])
    return sum(a) / 49


def med(a):
    a = sorted(a[:50])
    k = len(a)
    if k % 2 == 0:
        return (a[k // 2] + a[k // 2 + 1]) / 2
    else:
        return a[k // 2 + 1]


df_1 = pd.read_excel('Tables/разводы.xlsx', index_col='time')
df_2 = pd.read_excel('Tables/корзины за зарплату.xlsx', index_col='time')
df_3 = pd.read_excel('Tables/безработица.xlsx', index_col='time')
df_4 = pd.read_excel('Tables/безработица.xlsx', index_col='time')
df_5 = pd.read_excel('Tables/разводы на 1 брак.xlsx', index_col='time')
d = {'region': df_3.columns, 'разводы': [], 'корзины за зарплату': [], 'безработица': [], 'браки': [],
     'разводы на 1 брак': []}
for i in df_2:
        d['разводы'].append(middle(df_1[i]))
        d['корзины за зарплату'].append(middle(df_2[i]))
        d['безработица'].append(middle(df_3[i]))
        d['браки'].append(middle(df_4[i]))
        d['разводы на 1 брак'].append(middle(df_5[i]))
df_3 = pd.DataFrame(d)
df_3.to_excel('Tables/средние значения.xlsx', index=False)
