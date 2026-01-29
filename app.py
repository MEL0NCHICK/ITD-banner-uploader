import os

import config
from upload import upload, scandir
from config import *

codecs = ["image/jpeg", "image/gif", "audio/mpeg", "video/mp4", ]
pic = ""
codec = ""

print("=" * 50)
print("📁 ЗАГРУЗКА ФАЙЛА")

print("="*50+"\n  Привет, что ты хочешь загрузить в шапку??? \n   1. Фото\n   2.Гифка\n   3.Музыка\n   4.Видео\n")
ans = int(input("Ввод:"))

try:
    codec = codecs[ans-1]
except Exception as e:
    print("Так не бывает(((")
    exit()

text = ""

if ans == 1:
    text = "фото"
elif ans == 2:
    text = "гифку"
elif ans == 3:
    text = "музычку"
elif ans == 4:
    text = "видосик"
else:
    print("Так не бывает(((")
    exit()

print("\n"*3+"=" * 50)
print("📁 ЗАГРУЗКА ФАЙЛА (Ищет в папке files)")

print("=" * 50, f"\n  {text.capitalize()} значит, ну окей, а теперь выбери файл который загрузишь, только не зыбывай что ты загружаешь {text} и выбор не того типа файла может не загрузиться")
print("   Найденные файлы:\n")

files = scandir("files")
f2 = []
for i in files:
    f2.append([i.name, f"{round(os.path.getsize(f"files/{i.name}") / 1024 / 1024, 2)} Мб"])

col_width = max(len(str(item)) for row in f2 for item in row) + 2
filenames = []
count = 1
for row in f2:
    print(f"     {count}."+"   ".join(str(item).ljust(col_width) for item in row))
    filenames.append(row[0])
    count += 1
print(filenames)


ans = int(input("Ввод:"))

filename = filenames[ans-1]
upload(f"files/{filename}", codec, config.bearer_token)
