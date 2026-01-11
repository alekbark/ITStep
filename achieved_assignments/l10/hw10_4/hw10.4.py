# Задание №4
# Пользователь с клавиатуры вводит названия файлов, до тех пор, пока он не введет
# слово  quit. После завершения ввода программа должна записать в итоговый файл символы,
# которые  есть во всех перечисленных файлах (символы должны быть в каждом файле).

test_files = {
    "a.txt": "abcdef",
    "b.txt": "bcdefg",
    "c.txt": "cdefhi"
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

common_chars = None

for file_name in files:
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            chars = set(f.read())

            if common_chars is None:
                common_chars = chars

            else:
                common_chars &= chars
    except FileNotFoundError:
        print(f"Файл {file_name} не найден и был пропущен")

result_file = "result.txt"

with open(result_file, "w", encoding="utf-8") as f:
    if common_chars:
        f.write("".join(common_chars))
    else:
        f.write("")

print("Готово. Результат записан в result.txt")
