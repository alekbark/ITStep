test_files = {
    "a.txt": "Содержимое фвйла А.\nСтрока 2 файла А.",
    "b.txt": "Файл В.\nЕще одна строка.",
    "c.txt": "Текст из файла С."
}

for name, content in test_files.items():
    with open(name, "w", encoding="utf-8") as f:
        f.write(content)

files = []

while True:
    name = input("Введите имя файла (или quit для завершения): ")

    if name == "quit":
        break
    files.append(name)

result_file = "result.txt"

with open(result_file, "w", encoding="utf-8") as out:
    for file_name in files:
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                out.write(f.read())
                out.write("\n")
        except FileNotFoundError:
            print(f"Файл {file_name} не найден и был пропущен.")

print("Готово. Результат записан в result.txt")
