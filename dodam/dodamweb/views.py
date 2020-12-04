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
    name = book.book_name
    inbook = in_book.objects.filter(book_name = name)
    return render(request, 'spec.html', {
                    'book': book,
                    'inbook0': inbook[0],'inbook1': inbook[1],'inbook2': inbook[2],'inbook3': inbook[3],'inbook4': inbook[4],
    'inbook5': inbook[5],'inbook6': inbook[6], 'inbook7': inbook[7], 'inbook8': inbook[8], 'inbook9': inbook[9]})
    
'''
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    sql = "SELECT full_intro FROM dodamweb_book_info as A INNER JOIN dodamweb_in_book as B ON A.book_name = B.book_name WHERE A.book_name = "+book.book_name
    cur.execute(sql)
    rows = cur.fetchall()
    cols = [column[0] for column in cur.description]

    conn.close()
    '''

