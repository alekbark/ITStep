import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    "date": pd.date_range("2024-01-01", periods=100),
    "product": np.random.choice(["A", "B", "C"], size=100),
    "sales": np.random.randint(10, 100, size=100),
    "price": np.random.randint(100, 500, size=100)
}

df = pd.DataFrame(data)

# Круговой график долей продаж по товарам
sales_pie = df.groupby("product")["sales"].sum()
sales_pie.plot(kind="pie", autopct="%1.1f%%")
plt.title("Доли продаж по товарам")
plt.ylabel("")
plt.show()


# Разбивка по продажам от цены
df["price_category"] = pd.cut(
    df["price"],
    bins=[100, 200, 300, 400, 500]
)

price_bins = df['price_category'].value_counts().sort_index()
price_bins.plot(kind="bar", rot=0)
plt.title("Распределение по ценам")
plt.xlabel("Диапазон цен")
plt.ylabel("Количество")
plt.tight_layout()
plt.show()


# Средняя цена по товарам
average_price = df.groupby("product")["price"].mean().round().sort_values(ascending=False)
ax = average_price.plot(kind="bar", rot=0)

for i, v in enumerate(average_price):
    ax.text(i, v + 5, f"{v:.0f}", ha="center")

plt.title("Средняя цена по товарам")
plt.xlabel("Товар")
plt.ylabel("Цена")
plt.tight_layout()
plt.show()


# Продажи по месяцам
df["month"] = df["date"].dt.month_name()
df_filtered = df[df["month"] != "April"]
monthly_sales = df_filtered.groupby("month")["sales"].sum()
monthly_sales = monthly_sales.reindex(["January", "February", "March"])
ax = monthly_sales.plot(kind="bar", rot=0)

for i, v in enumerate(monthly_sales):
    ax.text(i, v + 20, int(v), ha="center")

plt.title("Продажи по месяцам")
plt.xlabel("Месяц")
plt.ylabel("Продажи")
plt.tight_layout()
plt.show()
plt.show()