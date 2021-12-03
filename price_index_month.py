import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy

df = pd.read_excel('1 StatSspace/result_zen_in_col1.xlsx', index_col='region')
a = df.index
d = {'region': df.index}
for i in df:
    for j in range(len(a)):
        if df[i][j] > 0:
            if i in d:
                d[i].append(df[i][j])
            else:
                d[i] = [df[i][j]]
        else:
            if i in d:
                d[i].append(0)
            else:
                d[i] = [0]
if numpy.NAN in d:
    d.pop(numpy.NAN)
for i in d:
    if i != 'region':
        r = [100]
        for j in range(1, len(d[i])):
            k = j - 1
            while k > -1 and d[i][k] == 0:
                k -= 1
            if k != -1:
                r.append((d[i][j] - d[i][k]) / d[i][k] * 10000)
            else:
                r.append(100)
        d[i] = r
df_1 = pd.DataFrame(d)
df_1.to_excel('Tables/индекс цен по месяцам.xlsx', index=False)
# df_1.plot()
# plt.show()
