import psycopg2

conn = psycopg2.connect(
    dbname="pgsql_exam_2",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("""
DROP TABLE IF EXISTS subscriptions;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS journals;
""")

cursor.execute("""
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);
""")

cursor.execute("""
CREATE TABLE journals (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100)
);
""")

cursor.execute("""
CREATE TABLE subscriptions (
    user_id INT REFERENCES users(id),
    journal_id INT REFERENCES journals(id),
    PRIMARY KEY (user_id, journal_id)
);
""")

conn.commit()

def create_user(cursor, name):
    cursor.execute("""
    INSERT INTO users (name) 
    VALUES (%s);
    """, (name,))

def create_journal(cursor, title):
    cursor.execute("""
    INSERT INTO journals (title) 
    VALUES (%s)
    """, (title,))

def subscribe(cursor, user_id, journal_id):
    cursor.execute("""
    INSERT INTO subscriptions (user_id, journal_id) 
    VALUES (%s, %s)
    """, (user_id, journal_id))

def unsubscribe(cursor, user_id, journal_id):
    cursor.execute("""
    DELETE FROM subscriptions 
    WHERE user_id = %s AND journal_id = %s
    """, (user_id, journal_id))

def get_all(cursor):
    cursor.execute("""
    SELECT u.name, j.title
    FROM subscriptions s
    JOIN users u ON u.id = s.user_id
    JOIN journals j ON j.id = s.journal_id
    """)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

create_user(cursor, 'Maksim')
create_user(cursor, 'Anna')

create_journal(cursor, 'Forbes')
create_journal(cursor, 'PopMMA')

subscribe(cursor, 1, 1)
subscribe(cursor, 1, 2)
subscribe(cursor, 2, 1)

conn.commit()

print("Подписки:")
get_all(cursor)

unsubscribe(cursor, 1, 2)
conn.commit()

print("После отписки:")
get_all(cursor)