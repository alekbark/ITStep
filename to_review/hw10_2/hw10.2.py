# Задание №2
# Написать программу транслитерации с русского на английский и наоборот. Данные для транслитерации
# берутся из файла и записываются в другой файл. Направление перевода определяется через меню пользователя.

input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "w", encoding="utf-8") as f:
    f.write("Привет, мир! Это текст траслитерации.")

ru_to_en = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d",
    "е": "e", "ё": "yo", "ж": "zh", "з": "z", "и": "i",
    "й": "y", "к": "k", "л": "l", "м": "m", "н": "n",
    "о": "o", "п": "p", "р": "r", "с": "s", "т": "t",
    "у": "u", "ф": "f", "х": "kh", "ц": "ts", "ч": "ch",
    "ш": "sh", "щ": "shch", "ы": "y", "э": "e",
    "ю": "yu", "я": "ya"
}

en_to_ru = {v: k for k, v in ru_to_en.items()}

print("Выберите направление транслитерации:")
print("1 - Русский → Английский")
print("2 - Английский → Русский")

choice = input("Ваш выбор: ")

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

result = ""

if choice == "1":
    for char in text:
        lower = char.lower()
        if lower in ru_to_en:
            trans = ru_to_en[lower]
            result += trans.capitalize() if char.isupper() else trans
        else:
            result += char

elif choice == "2":
    i = 0
    while i < len(text):
        matched = False
        for size in (4, 3, 2, 1):
            chunk = text[i:i + size].lower()
            if chunk in en_to_ru:
                trans = en_to_ru[chunk]
                result += trans.upper() if text[i].isupper() else trans
                i += size
                matched = True
                break
        if not matched:
            result += text[i]
            i += 1

else:
    print("Неверный выбор")
    exit()

with open(output_file, "w", encoding="utf-8") as f:
    f.write(result)

print(f"Готово. Результат был записан в {output_file}")