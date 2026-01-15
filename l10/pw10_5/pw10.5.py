# Работа с файлами и каталогами
# Задание №5

import re

input_file = "input.txt"

output_file = "output.txt"

sample_text = (
    "Это пример текста для проверки.\n"
    "В нём есть буквы, цифры 12345 и переносы строк.\n"
    "English words are also included.\n"
)

with open(input_file, "w", encoding="utf-8") as f:
    f.write(sample_text)
#
# with open(input_file, "r", encoding="utf-8") as f:
#     text = f.read()
#
# char_count = len(text)
#
# line_count = text.count("\n") + 1 if text else 0
#
# vowels_pattern = r"[аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU]"
# consonants_pattern = r"[бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]"
# digits_pattern = r"\d"
#
# vowels_count = len(re.findall(vowels_pattern, text))
#
# consonants_count = len(re.findall(consonants_pattern, text))
#
# digits_count = len(re.findall(digits_pattern, text))
#
# with open(output_file, "w", encoding="utf-8") as f:
#     f.write(f"Количество символов: {char_count}\n")
#     f.write(f"Количество строк: {line_count}\n")
#     f.write(f"Количество гласных букв: {vowels_count}\n")
#     f.write(f"Количество согласных букв: {consonants_count}\n")
#     f.write(f"Количество цифр: {digits_count}\n")
