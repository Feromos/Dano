import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy
import scipy.stats
import stats

plt.style.use('ggplot')
df = pd.read_excel('Tables/по округам.xlsx')
a = ['Республика Ингушетия', 'Чеченская Республика', 'Республика Тыва']
b = ['Магаданская область', 'Мурманская область', 'Камчатский край', 'Ямало-Ненецкий авт.округ', 'Тюменская область',
     'Сахалинская область', 'Чукотский авт.округ']
c = ['Кабардино-Балкарская Республика', 'Республика Северная  Осетия - Алания', 'Республика Татарстан',
     'Удмуртская Республика', 'Республика Бурятия', 'Ставропольский край', 'Республика Марий Эл', 'Республика Адыгея',
     'Республика Калмыкия', 'Карачаево-Черкесская Республика', 'Республика Мордовия', 'Чувашская Республика']
d = ['Еврейская авт.область', 'Новосибирская область', 'Приморский край', 'Калининградская область', 'Хабаровский край',
     'Амурская область']
s = ['г.Москва', 'Республика Татарстан']
x = []
y = []
t = 0
k = 0
m = 0
n = ''
for i in range(len(df['region'])):
    if df['region'][i] not in s:
        if type(df['region'][i]) != str:
            t += 1
            if t > k:
                break
        elif t > k - 1:
            if m < df['корзины за зарплату'][i]:
                m = df['корзины за зарплату'][i]
                n = df['region'][i]
            print(df['region'][i])
            x.append(df['разводы'][i])
            y.append(df['корзины за зарплату'][i])
            if df['region'][i] == 'Ярославская область':
                k = 1
            if df['region'][i] == 'г.Санкт-Петербург':
                k = 4
x = numpy.asarray(x)
y = numpy.asarray(y)
slope, intercept, r, *__ = scipy.stats.linregress(x, y)
line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=0, marker='s', label='Data points')
ax.plot(x, intercept + slope * x, label=line)
ax.set_xlabel('divorces')
ax.set_ylabel('wealth')
ax.legend(facecolor='white')
plt.title('Центральный, Северо-Западный и Приволжский округа')
plt.show()
