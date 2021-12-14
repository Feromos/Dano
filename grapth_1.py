import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy
import scipy.stats
import stats

plt.style.use('ggplot')
df_1 = pd.read_excel('Tables/количество потребительских корзин за зарплату(группы).xlsx')
d = {'Среднее': []}
for i in df_1:
    t = 0
    m = 0
    for j in df_1[i]:
        if j > 0:
            m += j
            t += 1
    if t == 0:
        d['Среднее'].append(numpy.NAN)
    else:
        d['Среднее'].append(m / t)
df_2 = pd.DataFrame(d)
df_2.plot()
plt.show()
