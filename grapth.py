import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy
import scipy.stats
import stats

plt.style.use('ggplot')
df_1 = pd.read_excel('Tables/чистые разводы.xlsx', index_col='time')
df_2 = pd.read_excel('Tables/чистые корзины.xlsx', index_col='time')
a = ['Республика Ингушетия', 'Чеченская Республика', 'Республика Тыва']
b = ['Магаданская область', 'Мурманская область', 'Камчатский край', 'Ямало-Ненецкий авт.округ', 'Тюменская область',
     'Сахалинская область', 'Чукотский авт.округ']
c = ['Кабардино-Балкарская Республика', 'Республика Северная  Осетия - Алания', 'Республика Татарстан',
     'Удмуртская Республика', 'Республика Бурятия', 'Ставропольский край', 'Республика Марий Эл', 'Республика Адыгея',
     'Республика Калмыкия', 'Карачаево-Черкесская Республика', 'Республика Мордовия', 'Чувашская Республика']
d = ['Еврейская авт.область', 'Новосибирская область', 'Приморский край', 'Калининградская область', 'Хабаровский край',
     'Амурская область']
x = []
y = []
t = 0
for i in df_1:
    if i != 'time' and i != 'г.Москва':
        if 'Un' in i:
            t += 1
            if t > 1:
                break
        if t>0:
            x.append(sum(df_1[i][:49]) / 49)
            y.append(sum(df_2[i][:49]) / 49)

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
