# Работа с файлами и каталогами
# Задание №1
# В текущей папке лежат две другие папки: video и sub. Создайте новую папку watch_me
# и переложите туда содержимое указанных папок (сами папки класть не надо).

import os
import shutil

import os
import shutil

base_dir = os.getcwd()

# Создаем папки и файлы

video_dir = os.path.join(base_dir, "video")
sub_dir = os.path.join(base_dir, "sub")

os.makedirs(sub_dir, exist_ok=True)
os.makedirs(video_dir, exist_ok=True)

with open(os.path.join(video_dir, "trailer.mp4"), "w", encoding="utf-8") as f:
    f.write("Trailer file")

with open(os.path.join(sub_dir, "movie.mp4"), "w", encoding="utf-8") as f:
    f.write("Video file")

clips_dir = os.path.join(video_dir, "clips")
os.makedirs(clips_dir, exist_ok=True)

with open(os.path.join(clips_dir, "clip1.mp4"), "w", encoding="utf-8") as f:
    f.write("Clip1 file")

with open(os.path.join(sub_dir, "movie.srt"), "w", encoding="utf-8") as f:
    f.write("Movie file")

with open(os.path.join(sub_dir, "trailer.srt"), "w", encoding="utf-8") as f:
    f.write("Trailer file")

target_dir = os.path.join(base_dir, "watch_me")
os.makedirs(target_dir, exist_ok=True)

source_folders = ["video", "sub"]
for folder in source_folders:
    folder_path = os.path.join(base_dir, folder)

    for item in os.listdir(folder_path):
        source_path = os.path.join(folder_path, item)
        destination_path = os.path.join(target_dir, item)

        shutil.move(source_path, destination_path)