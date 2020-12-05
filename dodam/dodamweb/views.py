from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import sqlite3
import json
import html

import compare_with
import random
from django.views.generic.edit import FormView

from dodamweb.forms import *
from django.db.models import Q

from dodamweb.models import *


# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'index.html', context)


def shelf(request):
    booklist = book_info.objects.all()
    #검색기능 구현
    if 'q' in request.GET:
        query = request.GET.get('q')
        search_booklist = book_info.objects.all().filter(Q(book_name__contains=query))
        return render(request,'shelf.html',{'booklist': search_booklist})
    return render(request, 'shelf.html', {'booklist':booklist})


def spec(request, pk):
    # pk 책정보
    book = book_info.objects.get(pk = pk)
    # 책속에서
    name = book.book_name
    inbook = in_book.objects.filter(book_name = name).values_list('full_intro', flat=True).distinct()

    dict = {'book': book}
    '''
    num = len(inbook)

    for j in range(0, num):
        i = str(j)
        dict['inbook' + i] = inbook[j]
    '''
    dict['inbook']= inbook

    # 감정
    emotion = compare_with.compare_with(book.short_intro)
    emo = music.objects.filter(mood = emotion)
    print(emo)
    random_music = random.choice(emo)
    print(random_music)
    dict['random_music'] = random_music.embedded_code



    return render(request, 'spec.html', dict)
    


