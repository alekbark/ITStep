# Работа с файлами и каталогами
# Задание №1

import os

# создаем файлы для проверки программы

test_files = [
    "song1.mp3",
    "song2.mp3",
    "track.flac",
    "voice.oga",
    "notes.txt"
]

for name in test_files:
    with open(name, "w") as f:
        f.write("test")

# здесь тело основной программы

# basedir = os.getcwd()
#
# extensions = ["mp3", 'flac', "oga"]
#
# for ext in extensions:
#     folder_path = os.path.join(basedir, ext)
#     if not os.path.exists(folder_path):
#         os.mkdir(folder_path)
#
# for file_name in os.listdir(basedir):
#     file_path = os.path.join(basedir, file_name)
#     if os.path.isfile(file_path):
#         name, ext = os.path.splitext(file_name)
#         ext = ext.lstrip(".")
#         if ext in extensions:
#             new_path = os.path.join(basedir, ext, file_name)
#             os.rename(file_path, new_path)