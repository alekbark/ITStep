# а) Создайте json файл в операционной системе, заполните его данными с сайта
# https://jsonplaceholder.typicode.com/todos/1
# б) Прочитайте этот файл в python-словарь.

import json
import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)

data = response.json()

with open("todo.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

with open("todo.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

print(loaded_data)