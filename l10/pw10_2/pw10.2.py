# Работа с файлами и каталогами
# Задание №2

import os
import shutil
from os import getcwd

# сначала готовим окружение

base_dir = os.getcwd()
folders = ["vasya", "mila"]
files = ["kursovaya.doc", "test.pdf", "notes.txt"]

for folder in folders:
    folder_path = os.path.join(base_dir,folder)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    for file_name in files:
        file_path = os.path.join(folder_path,file_name)

        if not os.path.exists(file_path):
            with open(file_path,"w", encoding="utf-8") as f:
                f.write(f"Файл {file_name} из папки {folder}")

# выполняем задание

for folder in folders:
    folder_path = os.path.join(base_dir,folder)

    for file_name in os.listdir(folder_path):
        source_file = os.path.join(folder_path,file_name)

        if os.path.isfile(source_file):
            new_name = f"{folder}_{file_name}"
            destination_file = os.path.join(base_dir,new_name)
            shutil.copy2(source_file,destination_file)