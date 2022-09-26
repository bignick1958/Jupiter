import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('P1_diamonds.csv', header=0)
data = data.drop('Unnamed: 0', axis=1)
data.head()

plt.hist(data['price'], bins=150)

# Добавление заголовка
plt.title("Частотный график: Цены на бриллианты \n", fontdict={'fontsize': 20, 'fontweight': 20, 'color': 'Green'})

plt.xlabel('Цена', fontdict={'fontsize': 12, 'fontweight': 20, 'color': 'darkred'})
plt.ylabel('Количество', fontdict={'fontsize': 12, 'fontweight': 20, 'color': 'darkred'})

plt.show

groupdata = data.groupby('cut').count()
groupdata
x_vals = []
y_vals = []
for i in [0,1,4,3,2]
    x_vals.append(groupdata.index[i])
    y_vals.append(groupdata.iloc[i,0])

plt.bar(x_vals, y_vals)
ply.title("Частотный график: Огранка бриллиантов \n", fontdict={'fontsize': 20, 'fontweight': 20, 'color': 'Green'})

plt.xlabel('Огранка', fontdict={'fontsize': 12, 'fontweight': 20, 'color': 'darkred'})
plt.ylabel('Количество', fontdict={'fontsize': 12, 'fontweight': 20, 'color': 'darkred'})

plt.show()