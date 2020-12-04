from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import sqlite3
import json


# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'index.html', context)


def shelf(request):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()

    cur.execute("SELECT * FROM dodamweb_book_info LIMIT 0,10")
    rows = cur.fetchall()
    context = {
        'book1': rows[0][2],
        'book2': rows[1][2],
        'book3': rows[2][2],
        'book4': rows[3][2],
        'book5': rows[4][2],
        'book6': rows[5][2],
        'book7': rows[6][2],
        'book8': rows[7][2],
        'book9': rows[8][2],
        'book10': rows[9][2],
    }
    return render(request, 'shelf.html', context)

'''
def shelf1(request):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()

    cur.execute("SELECT * FROM dodamweb_book_info LIMIT 0,10")
    rows = cur.fetchall()
    context = {
        'result': 'success',
        'books': rows,
    }
    return render(request, 'shelf.html', json.dumps(context), content_type='application/json')
'''

def spec(request):
    searchWord = request.GET.get('title')
    context = {
    }
    return render(request, 'spec.html')