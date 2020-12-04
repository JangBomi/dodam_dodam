from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import sqlite3
import json

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
    book = book_info.objects.get(pk = pk)
    return render(request, 'spec.html', {'book': book})