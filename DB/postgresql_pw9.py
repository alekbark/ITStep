import psycopg2

conn = psycopg2.connect(
    dbname="products_pw9",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# создаем таблицы
cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50)
);    
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    price NUMERIC,
    category_id INTEGER REFERENCES categories(id)
);
""")

conn.commit()

# заполнение таблицы категорий
cursor.execute("""
INSERT INTO categories (name) VALUES
('Dairy'),
('Fruit'),
('Meat')
RETURNING id;
""")

conn.commit()

# заполнение таблицы продуктов
cursor.execute("""
INSERT INTO products (name, price, category_id) VALUES
('Milk', 200, 1),
('Cheese', 500, 1),
('Apple', 150, 2),
('Banana', 120, 2),
('Beef', 900, 3);
""")

conn.commit()


print("Задание 1 - Средняя цена по категориям")

cursor.execute("""
SELECT c.name, AVG(p.price)
FROM products p
JOIN categories c ON p.category_id = c.id
GROUP BY c.name;
""")

for row in cursor.fetchall():
    print(row)

print("\nЗадание 2 - HAVING  (средняя цена > 200)")

cursor.execute("""
SELECT c.name, AVG(p.price)
FROM products p
JOIN categories c ON p.category_id = c.id
GROUP BY c.name
HAVING AVG(p.price) > 200;
""")

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()