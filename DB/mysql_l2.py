import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Zz123456'
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS company_db")

cursor.execute("CREATE USER IF NOT EXISTS 'new_user'@'localhost' IDENTIFIED BY '1234'")

cursor.execute("GRANT ALL PRIVILEGES ON company_db.* TO 'new_user'@'localhost'")

connection.commit()

cursor.execute("USE company_db")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS salary (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL
)
""")

cursor.execute(
    "INSERT INTO Salary (title) VALUES (%s)",
    ("Danil Kolbasenko",)
)

connection.commit()

cursor.close()
connection.close()
print("Готово")