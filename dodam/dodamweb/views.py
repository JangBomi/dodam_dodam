from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import sqlite3
import json

import compare_with
import random

from dodamweb.models import *


# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'index.html', context)


def shelf(request):
    booklist = book_info.objects.all()
    return render(request, 'shelf.html', {'booklist':booklist})


def spec(request, pk):
    # pk 책정보
    book = book_info.objects.get(pk = pk)
    # 책속에서
    name = book.book_name
    inbook = in_book.objects.filter(book_name = name).values_list('full_intro', flat=True).distinct()
    dict = {'book': book}
    num = len(inbook)

    for j in range(0, num):
        i = str(j)
        dict['inbook' + i] = inbook[j]

    # 감정
    emotion = compare_with.compare_with(book.short_intro)
    emo = music.objects.filter(mood = emotion)
    print(emo)
    random_music = random.choice(emo)
    print(random_music)
    dict['random_music'] = random_music



    return render(request, 'spec.html', dict)
    


