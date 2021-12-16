import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy

df = pd.read_excel('1 StatSspace/result_dem3_col5.xlsx', index_col='region')
d = {'time': df.columns}
for i in range(len(df.index)):
    for j in range(len(df.columns) - 9):
        if df.index[i] in d:
            d[df.index[i]].append(df[df.columns[j]][i])
        else:
            d[df.index[i]] = [df[df.columns[j]][i]]
for i in d:
    if i != 'time':
        for j in range(len(d[i])):
            # if not d[i][j] > 0 and (j < 50 or (j == 61 and d[i][j - 1] > 0)):
            if not d[i][j] > 0:
                t = 1
                m = 0
                k = 0
                while t < 5:
                    if (j - t < 0) or not d[i][j - t] > 0:
                        k += 1
                    else:
                        m += d[i][j - t]
                    if (j + t >= len(d[i])) or not d[i][j + t] > 0:
                        k += 1
                    else:
                        m += d[i][j + t]
                    t += 1
                if 2 * t - k - 2 != 0:
                    d[i][j] = m / (2 * t - k - 2)
d['time'] = d['time'][:len(d['time']) - 9]
df_1 = pd.DataFrame(d)
df_1.to_excel('Tables/браки.xlsx', index=False)
# df_1.plot()
# plt.show()
