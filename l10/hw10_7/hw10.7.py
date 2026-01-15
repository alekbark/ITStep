# Задание №3
# В текущей папке лежит файл list.tsv, в котором с новой строки написаны имена
# некоторых других файлов этой папки. Создайте папку list и переложите в неё данные файлы.
import os
import shutil

base_dir = os.getcwd()

list_file = os.path.join(base_dir, 'list.tsv')

target_dir = os.path.join(base_dir, 'list')

os.makedirs(target_dir, exist_ok=True)

with open(list_file, 'r', encoding="utf-8") as f:
    for line in f:
        filename = line.strip()

        if not filename:
            continue

        source_path = os.path.join(base_dir, filename)
        destination_path = os.path.join(target_dir, filename)

        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)
        else:
            print(f"Файл {filename} не найден и был пропущен")

