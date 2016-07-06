__author__ = 'rj'

from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
import datetime

def hello(request):
    current_date = datetime.datetime.now()
    return render_to_response('alaki/current_datetime.html',locals())

def hours_ahead(request,offset):

    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def scheduler(request):
    #current_date = datetime.datetime.now()
    return render_to_response('scheduler/scheduler.html',locals())