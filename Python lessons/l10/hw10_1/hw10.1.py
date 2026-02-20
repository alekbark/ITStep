# Задание №1
# Дан текстовый файл. Необходимо создать новый файл убрав из него все неприемлемые слова.
# Список неприемлемых слов находится в другом файле.


import re

# text_file = "text.txt"
# bad_words_file = "bad_words.txt"
# result_file = "clean_text.txt"

# with open(text_file, "w", encoding="utf-8") as f:
#     f.write(
#         "Это плохо.\n"
#         "Иногда это бывает УЖАСНО плохо.\n"
#         "Но чаще всего всё хорошо!\n"
#     )
#
# with open(bad_words_file, "w", encoding="utf-8") as f:
#     f.write("плохо\nужасно\n")


# with open(bad_words_file, "r", encoding="utf-8") as f:
#     bad_words = [w.strip() for w in f if w.strip()]
#
# with open(text_file, "r", encoding="utf-8") as f:
#     text = f.read()
#
# pattern = r"\b(" + "|".join(map(re.escape, bad_words)) + r")\b"
#
# clean_text = re.sub(pattern, "", text, flags=re.IGNORECASE)
#
# clean_text = re.sub(r'\s{2,}', ' ', clean_text)
#
# with open(result_file, "w", encoding="utf-8") as f:
#     f.write(clean_text)