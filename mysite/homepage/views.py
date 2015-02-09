from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect

import datetime
import requests

# Create your views here.
l = loader
def base(request):
    time = datetime.datetime.now().strftime('%Y')
    t = l.get_template('base.html')
    c = Context({
        'time': time,
    })
    return HttpResponse(t.render(c))
