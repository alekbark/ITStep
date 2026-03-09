import psycopg2

conn = psycopg2.connect(
    dbname="products_pw9",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# удаляем старые таблицы
cursor.execute("""
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS clients;
""")

# создадим таблицы для всех трех заданий

cursor.execute("""

CREATE TABLE clients (
id SERIAL PRIMARY KEY,
name VARCHAR(50),
city VARCHAR(50),
country VARCHAR(50)
);

CREATE TABLE products (
id SERIAL PRIMARY KEY,
name VARCHAR(50),
price NUMERIC,
category VARCHAR(50)
);

CREATE TABLE orders (
id SERIAL PRIMARY KEY,
client_id INTEGER NOT NULL,
amount NUMERIC
);

""")

# Задание №1
# Создайте запрос, который будет выводить список всех городов из таблицы
# клиентов, а затем группирует их по странам. Затем используйте HAVING,
# чтобы вывести список стран, у которых более 3 городов.

# заполняем таблицу данными

cursor.execute("""
INSERT INTO clients (name, city, country) VALUES
('Ivan', 'Moscow', 'Russia'),
('Anna', 'Kazan', 'Russia'),
('Sergey', 'Samara', 'Russia'),
('Olga', 'Sochi', 'Russia'),
('Pavel', 'Novosibirsk', 'Russia'),

('John', 'New York', 'USA'),
('Kate', 'Chicago', 'USA'),
('Mike', 'Boston', 'USA'),

('Pierre', 'Paris', 'France'),
('Luc', 'Lyon', 'France');
""")

conn.commit()

cursor.execute("""
SELECT c.country, COUNT(c.city)
FROM clients c
group by c.country
""")

print("Задание 1\n")
for row in cursor.fetchall():
    print(row)

print()

cursor.execute("""
SELECT c.country, COUNT(c.city)
FROM clients c
group by c.country
HAVING COUNT(c.city) > 3;
""")
for row in cursor.fetchall():
    print(row)

print()

# Задание №2
# Создайте запрос, который будет выводить список всех продуктов и среднюю
# цену продукта для каждой категории продуктов. Затем группируйте
# результаты по категориям, и используйте HAVING, чтобы вывести список
# категорий, у которых средняя цена продукта больше 50.

cursor.execute("""
INSERT INTO products (name, price, category) VALUES
('Milk', 40, 'Dairy'),
('Cheese', 120, 'Dairy'),
('Yogurt', 60, 'Dairy'),

('Apple', 30, 'Fruit'),
('Banana', 25, 'Fruit'),
('Orange', 55, 'Fruit'),

('Beef', 200, 'Meat'),
('Chicken', 90, 'Meat'),
('Pork', 150, 'Meat'),

('Bread', 35, 'Bakery'),
('Croissant', 70, 'Bakery'),
('Baguette', 65, 'Bakery');
""")

conn.commit()

print("Задание 2\n")

cursor.execute("""
SELECT p.name FROM products p;
""")

for row in cursor.fetchall():
    print(row)

print()

cursor.execute("""
SELECT p.category, AVG(p.price)
FROM products p
GROUP by p.category;
""")

for row in cursor.fetchall():
    print(row)

print()

cursor.execute("""
SELECT p.category, AVG(p.price)
FROM products p
GROUP by category
HAVING AVG(p.price) > 50;
""")

for row in cursor.fetchall():
    print(row)

print()

# Задание №3
# Создайте запрос, который будет выводить список всех заказов, и сумму
# заказа для каждого клиента. Затем группируйте результаты по клиентам, и
# используйте HAVING, чтобы вывести список клиентов, у которых сумма
# заказов больше 10 000

cursor.execute("""
INSERT INTO orders (client_id, amount) VALUES
(1, 4000),
(1, 7000),

(2, 2000),
(2, 1500),

(3, 6000),
(3, 5000),

(4, 1200),

(5, 9000),
(5, 3000),

(6, 2000),
(7, 2500),
(8, 1500);
""")

conn.commit()

print("Задание 3\n")

print("Все id клинетов с суммой их заказов")
cursor.execute("""
SELECT o.client_id, SUM(o.amount)
FROM orders o
GROUP by o.client_id
""")

for row in cursor.fetchall():
    print(row)

print("\nИмена клиентов с суммой заказов больше 10000:")
# специально в первом выводе оставил id, а во второй имена для разнообразия

cursor.execute("""
SELECT c.name, SUM(o.amount)
FROM orders o
JOIN clients c ON o.client_id = c.id
GROUP by c.name
HAVING SUM(o.amount) > 10000;
""")

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()