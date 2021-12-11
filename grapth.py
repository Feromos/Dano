import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy
import scipy.stats
import stats

plt.style.use('ggplot')
df_1 = pd.read_excel('Tables/корреляция_безработица_разводы.xlsx', index_col='time')
x = []
y = []
for i in df_1:
    if i != 'time':
        t1, t2, m1, m2 = 0, 0, 0, 0
        f = True
        for j in range(len(df_1[i]) - 2):
            if j == 24:
                f = False
            else:
                if f:
                    if df_1[i][j] != 0:
                        m1 += df_1[i][j]
                        t1 += 1
                else:
                    if df_1[i][j] != 0:
                        m2 += df_1[i][j]
                        t2 += 1
        x.append(m1 / t1)
        y.append(m2 / t2)
x = numpy.asarray(x)
y = numpy.asarray(y)
slope, intercept, r, *__ = scipy.stats.linregress(x, y)
line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=0, marker='s', label='Data points')
ax.plot(x, intercept + slope * x, label=line)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(facecolor='white')
plt.title('Корреляция разводов и безработицы')
plt.show()
