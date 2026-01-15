# Задание №2
# В текущей папке лежат файлы типа Nina_Stoletova.jpg, Misha_Perelman.jpg и т.п.
# Переименуйте их переставив имя и фамилию местами.

import os

base_dir = os.getcwd()

for filename in os.listdir(base_dir):
    if not filename.endswith(".jpg"):
        continue
    name, ext = os.path.splitext(filename)

    if "_" not in name:
        continue

    first_name, last_name = name.split("_", 1)

    new_filename = f"{last_name}_{first_name}{ext}"

    old_path = os.path.join(base_dir, filename)
    new_path = os.path.join(base_dir, new_filename)

    os.rename(old_path, new_path)

