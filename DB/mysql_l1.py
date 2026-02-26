import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Zz123456",
    database="test_db"
)

cursor = connection.cursor()

cursor.execute("SELECT VERSION()")

row = cursor.fetchone()

while row:
    print(row[0])
    row = cursor.fetchone()

cursor.close()
connection.close()