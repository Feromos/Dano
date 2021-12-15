import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy
import scipy.stats
import stats

plt.style.use('ggplot')
df_1 = pd.read_excel('Tables/разводы.xlsx', index_col='time')
df_2 = pd.read_excel('Tables/корзины за зарплату.xlsx', index_col='time')
d = {'регрессия': df_1.columns}
for i in df_1:
    x = df_1[i][1:49]
    y = df_2[i][1:49]
    x = numpy.asarray(x)
    y = numpy.asarray(y)
    slope, intercept, r, *__ = scipy.stats.linregress(x, y)
    d[i] = [slope]
# df_3 = pd.DataFrame(d)
# df_3.to_excel('Tables/регрессия разводов и доходов.xlsx', index=False)
x = []
y = []
print(d)
for i in df_1:
    if d[i][0] <= -0.4:
        x.append(sum(df_1[i][1:49]) / 48)
        y.append(sum(df_2[i][1:49]) / 48)
x = numpy.asarray(x)
y = numpy.asarray(y)
slope, intercept, r, *__ = scipy.stats.linregress(x, y)
line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=0, marker='s', label='Data points')
ax.plot(x, intercept + slope * x, label=line)
ax.set_xlabel('разводы')
ax.set_ylabel('доходы')
ax.legend(facecolor='white')
plt.title('Регрессия разводов и доходов')
plt.show()
