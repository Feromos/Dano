import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy

df_1 = pd.read_excel('Tables/разводы.xlsx', index_col='time')
df_2 = pd.read_excel('Tables/браки.xlsx', index_col='time')
d = {'time': df_1.index}
for i in range(len(df_1.columns)):
    for j in range(len(df_1[df_1.columns[i]])):
        k = 0
        if df_2[df_1.columns[i]][j] != 0:
            k = df_1[df_1.columns[i]][j] / df_2[df_1.columns[i]][j]
        if df_1.columns[i] in d:
            d[df_1.columns[i]].append(k)
        else:
            d[df_1.columns[i]] = [k]

df_3 = pd.DataFrame(d)
df_3.to_excel('Tables/разводы на 1 брак.xlsx', index=False)
# df_1.plot()
# plt.show()
