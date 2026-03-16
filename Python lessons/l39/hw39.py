# Домашнее задание №39: Работа с большими данными - pandas, numpy,
# mathplotlib

# Задание №1
# а) Создайте массив данных, например с продажей товаров, для будущего анализа.
# б) Используйте стандартные математические методы из библиотек для анализа данных:
# среднее, средневзвешенное, максимальное-минимальное и другие.

import pandas as pd
import numpy as np

# a)
# создаем данные
data = {
    "Day": np.arange(1, 11),
    "Sales": [120, 150, 170, 130, 200, 210, 190, 220, 250, 230]
}

# создаем DataFrame
df = pd.DataFrame(data)

print("Таблица продаж:")
print(df)

# б)
# среднее значение продаж
mean_sales = np.mean(df["Sales"])

# максимальные продажи
max_sales = np.max(df["Sales"])

# минимальные продажи
min_sales = np.min(df["Sales"])

# медиана
median_sales = np.median(df["Sales"])

# стандартное отклонение
std_sales = np.std(df["Sales"])

print("\nАнализ данных:")
print("Среднее значение:", mean_sales)
print("Максимальлное значение",max_sales)
print("Минимальное значение",min_sales)
print("Медиана", median_sales)
print("Стандартное отклонение", std_sales)

# средневзвешенное значение
weights = np.array([10, 12, 15, 9, 20, 22, 18, 25, 30, 27])

weighted_mean = np.average(df["Sales"], weights=weights)

print("Средневзвешенное значение:", weighted_mean)

# график
import matplotlib.pyplot as plt

plt.plot(df["Day"], df["Sales"], marker="o")
plt.title("Продажи по дням")
plt.xlabel("День")
plt.ylabel("Продажи")
plt.grid()

plt.show()
