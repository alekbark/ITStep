# а) Создайте json файл в операционной системе, заполните его данными с сайта
# https://jsonplaceholder.typicode.com/todos/
# б) Прочитайте этот файл в массив python-словарей.
# в) Запишите каждый из этих словарей в отдельный json-файл.

import json
import requests
from pathlib import Path

url = "https://jsonplaceholder.typicode.com/todos/"

response = requests.get(url)
data = response.json()

with open("todos.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

with open("todos.json", "r", encoding="utf-8") as file:
    todos = json.load(file)

Path("todos").mkdir(exist_ok=True)

for todo in todos:
    filename = f"todos/todo_{todo['id']}.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(todo, file, ensure_ascii=False, indent=4)

