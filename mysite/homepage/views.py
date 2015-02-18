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
    mware1 = next(request.generator)
    mware2 = next(request.generator)
    mware3 = next(request.generator)
    print("4th time:")
    print(next(request.generator))
    print("5th time:")
    print(next(request.generator))
    print("6th time:")
    print(next(request.generator))
    c = Context({
        'time': time,
        'mware1': mware1,
        'mware2': mware2,
        'mware3': mware3,
    })
    return HttpResponse(t.render(c))
