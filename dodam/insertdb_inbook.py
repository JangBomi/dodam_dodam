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

CSV_PATH_INBOOK = './csv/in_book.csv'

with open(CSV_PATH_INBOOK, "r", encoding="utf-8-sig") as csvfile:
    data_reader = csv.reader(csvfile)

    for row in data_reader:
        row[0] = row[0].replace('"',"");
        in_book.objects.create(  # 5. class명.objects.create
            book_name=row[0],
            full_intro=row[1],
            # 6
        )