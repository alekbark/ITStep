import psycopg2

conn = psycopg2.connect(
    dbname="postgresql_hw10",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("""
DROP TABLE IF EXISTS rides CASCADE;
DROP TABLE IF EXISTS clients CASCADE;
DROP TABLE IF EXISTS drivers CASCADE;
""")

# создаем таблицы
cursor.execute("""
CREATE TABLE drivers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    rating FLOAT DEFAULT 5,
    rating_count INT DEFAULT 0
);
""")

cursor.execute("""
CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE rides (
    id SERIAL PRIMARY KEY,
    client_id INT REFERENCES clients(id),
    driver_id INT REFERENCES drivers(id),
    rating INT
);
""")

# функция для обновления рейтинга
cursor.execute("""
CREATE OR REPLACE FUNCTION update_driver_rating ()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN

UPDATE drivers
SET
rating = (rating * rating_count + NEW.rating) / (rating_count + 1),
rating_count = rating_count + 1
WHERE id = NEW.driver_id;

RETURN NEW;

END;
$$;
""")

cursor.execute("""
CREATE TRIGGER update_driver_rating
AFTER INSERT ON rides
FOR EACH ROW
EXECUTE FUNCTION update_driver_rating();    
""")

conn.commit()

# добавляем водителя
def add_driver(name):
    cursor.execute(
        "INSERT INTO drivers (name) VALUES (%s) RETURNING id;",
        (name,)
    )
    driver_id = cursor.fetchone()[0]
    conn.commit()
    print(f"Driver created with id {driver_id}")

# добавляем клиента
def add_client(name):
    cursor.execute(
        "INSERT INTO clients (name) VALUES (%s) RETURNING id;",
        (name,)
    )
    client_id = cursor.fetchone()[0]
    conn.commit()
    print(f"Client created with id {client_id}")

# создаем поездку
def create_ride(client_id, driver_id, rating):
    cursor.execute(
        """
        INSERT INTO rides (client_id, driver_id, rating)
        VALUES (%s, %s, %s)
        """,
        (client_id, driver_id, rating)
    )
    conn.commit()
    print(f"Ride created with client {client_id} and driver {driver_id}")

# выводим информацию о рейтингах водителей
def show_drivers():
    cursor.execute("SELECT id, name, rating, rating_count FROM drivers")
    drivers = cursor.fetchall()

    print("\nDrivers:")
    for d in drivers:
        print(f"id={d[0]} name={d[1]} rating={d[2]} votes={d[3]}")

# тест
add_driver("Andrey")
add_client("Vitaliy")

create_ride(1, 1, 5)
create_ride(1, 1, 4)

show_drivers()

cursor.close()
conn.close()