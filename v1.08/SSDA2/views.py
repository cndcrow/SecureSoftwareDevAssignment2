from django.template.loader import get_template
from django.shortcuts import render
from django.template import Context
from django.http import HttpResponse
import datetime

def curr_date(request):
    now = datetime.datetime.now()
    return render(request, 'curr_date.html', {'curr_date': now})
