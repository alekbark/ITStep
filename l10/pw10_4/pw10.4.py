# Работа с файлами и каталогами
# Задание №4

import os

base_dir = os.getcwd()

test_files = [
    "2019-03-08.jpg",
    "2019-04-09.jpg",
    "2019-01-16.jpg",
    "2019-01-17.jpg",
    "2019-06-28.jpg",
]

for file_name in test_files:
    file_path = os.path.join(base_dir, file_name)

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"Test file {file_name}")

# jpg_files = []
#
# for file_name in os.listdir(base_dir):
#     if file_name.endswith(".jpg"):
#         jpg_files.append(file_name)
#
# jpg_files.sort()
#
# for index, file_name in enumerate(jpg_files, start=1):
#     old_path = os.path.join(base_dir, file_name)
#     new_name = f"{index}.jpg"
#     new_path = os.path.join(base_dir, new_name)
#     os.rename(old_path, new_path)

