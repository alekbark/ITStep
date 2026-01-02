# Работа с файлами и каталогами
# Задание №3

import os

base_dir = os.getcwd()

test_files = [
    "S0101.mkv",
    "S0102.mkv",
    "S0201.mkv",
    "S0202.mkv",
    "readme.txt"
]

for file_name in test_files:
    file_path = os.path.join(base_dir, file_name)

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"Test file {file_name}")

seasons = ["S01", "S02"]

for season in seasons:
    season_folder = os.path.join(base_dir, season)

    if not os.path.exists(season_folder):
        os.mkdir(season_folder)

for file_name in os.listdir(base_dir):
    file_path = os.path.join(base_dir, file_name)
    if os.path.isfile(file_path):
        for season in seasons:
            if file_name.startswith(season):
                new_path = os.path.join(base_dir, season, file_name)
                os.rename(file_path, new_path)
