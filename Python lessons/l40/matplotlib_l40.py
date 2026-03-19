import matplotlib.pyplot as plt
import numpy as np

# matplotlib.pyplot as plt - plot - это построить график
# scatter - разброс точек
# year = [1950, 1975, 2000, 2018]
# population = [2.12, 3.681, 5.312, 6.981]
#
# plt.scatter(year, population)
# plt.show()

# hist - гистограмма
# values = [0, 1.2, 1.3, 1.9, 4.3, 2.5, 2.7, 4.3, 1.3, 3.9]
# plt.hist(values, bins=5, color='blue', edgecolor='black')
# plt.show()

# linspace = line + space = равномерно разбить отрезок
# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# cos, sin = np.cos(X), np.sin(X)
#
# plt.plot(X, cos, color='blue', label='cosine')
# plt.plot(X, sin, color='red', label='sine')
# plt.legend(loc='upper left', frameon=False)
#
# plt.show()

# x = np.linspace(0, 10, 100)
# y = np.sin(x)
#
# fig, ax = plt.subplots(figsize=(16,10))
#
# ax.plot(x, y, label='Синусоидальная волна')
#
# ax.set_title("Cюжет")
# ax.legend()
# plt.show()

# x = np.linspace(0, 10, 200)
# y1 = np.sin(x)
# y2 = np.cos(x)
#
# fig, ax = plt.subplots(figsize=(9,5))
# ax.plot(x, y1, label='sin', lw=2.5)
# ax.plot(x, y2, label='cos', ls='--', lw=2)
# ax.legend()
# ax.grid(True, alpha=0.3)
# plt.show()

# data = np.random.normal(0, 1.5, 5000)
# fig, ax = plt.subplots(figsize=(8,5))
# ax.hist(data, bins=40, color='cornflowerblue', edgecolor='white')
# ax.set_title('Гистограмма')
# plt.show()

# labels = ['Продукты','Транспорт','Жильё','Прочее']
# sizes = [35, 18, 27, 20]
# fig, ax = plt.subplots(figsize=(7,7))
# ax.pie(sizes, labels=labels, autopct='%1.0f%%', shadow=True)
# ax.set_title('Структура расходов')
# plt.show()

# group1 = np.random.normal(100,15,200)
# group2 = np.random.normal(110,20,200)
# fig, ax = plt.subplots(figsize=(7,5))
# ax.boxplot([group1, group2], labels=['A','B'], patch_artist=True)
# plt.show()

# x = np.random.rand(150)*100
# y = 2*x + np.random.normal(0,15,150)
# fig, ax = plt.subplots(figsize=(8,6))
# ax.scatter(x, y, c=y, cmap='viridis', s=60, alpha=0.8)
# plt.show()

# cat = ['Янв','Фев','Мар','Апр']
# val = [120,180,150,220]
# fig, ax = plt.subplots(figsize=(8,5))
# ax.bar(cat, val, color='salmon')
# for i,v in enumerate(val):
#     ax.text(i, v+3, str(v), ha='center')
# plt.show()