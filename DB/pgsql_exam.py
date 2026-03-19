import psycopg2

conn = psycopg2.connect(
    dbname="pgsql_exam",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# Удаляем таблицы, если уже есть
cursor.execute("""
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS new_orders;
""")

# Таблица клиентов
cursor.execute("""
CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    city VARCHAR(255),
    age INT
);
""")

# Таблица заказов
cursor.execute("""
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    client_id INT REFERENCES clients(id),
    product VARCHAR(255),
    amount DECIMAL,
    order_date DATE               
);
""")

conn.commit()
print("Таблицы созданы")

# Добавляем клиентов и заказы

cursor.execute("""
INSERT INTO clients (name, city, age) VALUES
('Olga', 'Pavlodar', 25),
('Tatyana', 'Almaty', 27),
('Mark', 'Astana', 21),
('Afanasiy', 'Aktau', 37);
""")

cursor.execute("""
INSERT INTO orders (client_id, product, amount, order_date) VALUES
(1, 'Laptop', 1200, '2024-01-10'),
(1, 'Mouse', 25, '2024-01-12'),
(2, 'Phone', 800, '2024-02-05'),
(3, 'Tablet', 400, '2024-03-01'),
(4, 'Shaver', 50, '2024-04-05');
""")

conn.commit()
print("Заказы добавлены")

# Задание №1
# Напишите SQL-запрос, который извлекает данные из двух таблиц, используя оператор JOIN.

# cursor.execute("""
# SELECT
#     c.id,
#     c.name,
#     c.city,
#     o.order_date
# FROM clients c
# JOIN orders o
# ON o.client_id = c.id
# """)

# 2. Напишите запрос, который группирует данные и возвращает среднее значение для каждой группы.

# cursor.execute("""
# SELECT
#     c.name,
#     ROUND(AVG(o.amount), 2) AS avg_order
# FROM orders o
# JOIN clients c ON c.id = o.client_id
# GROUP BY c.name
# """)

# 3. Напишите запрос, который выбирает все строки из таблицы, где значение одного поля находится в списке определенных значений.

# cursor.execute("""
# SELECT c.name
# FROM clients c
# WHERE c.city IN ('Pavlodar', 'Astana')
# """)

# 4. Напишите запрос, который возвращает количество строк в таблице.

# cursor.execute("""
# SELECT COUNT(*) FROM orders;
# """)

# 5. Напишите запрос, который изменяет значение поля в определенной строке таблицы.

# cursor.execute("""
# UPDATE clients
# SET city = 'Pavlodar'
# WHERE name = 'Mark'
# """)
# conn.commit()
#
# cursor.execute("""
# SELECT * FROM clients
# """)

# 6. Напишите запрос, который удаляет все строки из таблицы, удовлетворяющие определенному условию.

# cursor.execute("""
# DELETE FROM orders
# WHERE amount < 1000;
# """)
# conn.commit()
#
# cursor.execute("""
# SELECT * FROM orders;
# """)

# 7. Напишите запрос, который создает новую таблицу на основе существующей таблицы.

# cursor.execute("""
# CREATE TABLE new_orders AS
# SELECT * FROM orders;
# """)
# conn.commit()
#
# cursor.execute("""
# SELECT * FROM new_orders;
# """)

# 8. Напишите запрос, который добавляет новую строку в таблицу.

# cursor.execute("""
# INSERT INTO clients (name, city, age)
# VALUES ('Alex', 'Karaganda', 30);
# """)
# conn.commit()
#
# cursor.execute("""
# SELECT * FROM clients;;
# """)

# 9. Напишите запрос, который удаляет таблицу.
# Есть в начале кода

# 10. Напишите запрос, который возвращает уникальные значения из определенного поля таблицы.

# cursor.execute("""
# SELECT DISTINCT city FROM clients;
# """)
#
# rows = cursor.fetchall()
# for row in rows:
#     print(row)


cursor.close()
conn.close()