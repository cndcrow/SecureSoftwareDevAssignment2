import sqlite3
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
import datetime

def home(request):
    return HttpResponse("home page!")

def hello(request):
    return HttpResponse("Hello World!")

def curr_date(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body> In %s hour(s), it will be %s </body></html>" % (offset, dt) 
    return HttpResponse(html)

def login(request):
    return render(request, 'login.html')

def try_login(request):
    if 'q' in request.GET and request.GET['q']:
        message = request.GET['q']
	db = sqlite3.connect('db.sqlite3')
	cursor = db.cursor()
	cursor.execute("INSERT INTO numbers(number) VALUES(?)", [message])
	message2 = cursor.execute("SELECT number from numbers")
	db.commit()
    return HttpResponse(message2)
