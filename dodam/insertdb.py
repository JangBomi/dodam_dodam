import csv
import os
import django
import sys



os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dodam.settings")  # 1. 여기서 프로젝트명.settings입력
django.setup()

# 위의 과정까지가 python manage.py shell을 키는 것과 비슷한 효과

from dodamweb.models import *  # 2. App이름.models

CSV_PATH = './csv/bookinfo.csv'  # 3. csv 파일 경로

with open(CSV_PATH, "r", encoding="utf-8") as csvfile:  # 4. newline =''
    data_reader = csv.reader(csvfile)

    for row in data_reader:
        book_info.objects.create(  # 5. class명.objects.create
            book_name=row[0],
            writer=row[1],
            book_img=row[2],
            short_intro =row[3],
            url = row[4],
            # 6
        )



CSV_PATH_MUSIC = './csv/music.csv'

with open(CSV_PATH_MUSIC, "r", encoding="utf-8") as csvfile:
    data_reader = csv.reader(csvfile)

    for row in data_reader:
        music.objects.create(  # 5. class명.objects.create
            music_name=row[0],
            singer=row[1],
            mood = row[2],
            embedded_code = row[3],
            # 6
        )
