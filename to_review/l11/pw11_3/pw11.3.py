# в) Сгенерируйте 100 словарей и запишите их в один json-файл.

import json

data = []

for i in range(1, 101):
    data.append({
        "id": i,
        "title": f"task {i}",
        "completed": i % 2 == 0
    })

with open('tasks.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

