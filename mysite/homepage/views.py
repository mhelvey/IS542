import datetime
from django.shortcuts import render, render_to_response
from django.template import Context, loader
from django.http import HttpResponse
from django import forms
from homepage import models as hmod
from django.http import JsonResponse
from lib.customform import CustomForm
from lib.widgets import DatePickWidget
from lib.table import Table


# Create your views here.
l = loader


def base(request):
    time = datetime.datetime.now().strftime('%Y')
    t = l.get_template('base.html')
    mware1 = next(request.generator)
    mware2 = next(request.generator)
    mware3 = next(request.generator)
    c = Context({
        'time': time,
        'mware1': mware1,
        'mware2': mware2,
        'mware3': mware3,
    })
    return HttpResponse(t.render(c))


def form(request):
    form = SampleForm(request)
    if request.method == 'POST':
        form = SampleForm(request)
    t = l.get_template('form.html')
    c = Context({
        'form': form,
    })

    return HttpResponse(t.render(c))


class SampleForm(CustomForm):
    def init(self):
        self.fields['date'] = forms.DateTimeField(widget=DatePickWidget)


def gallery(request):
    images = hmod.GalleryImage .objects.all()
    t = l.get_template('gallery.html')
    c = Context({
        'images': images,
    })

    return HttpResponse(t.render(c))


def table(request, tpage=0):
    print(tpage)
    params = {}
    params['initial_page'] = 0
    # tpage = request.REQUEST.get('page')
    if '/page/' not in request.path :
        return render_to_response('table.html', params)
    else:
        params = get_table(request, tpage)
        return JsonResponse(params)


ROWS_PER_PAGE = 5


def get_table(request, tpage):
    params = {}
    try:
        page = int(tpage)
        #page = 5
    except ValueError:
        page = 0

    qry = hmod.User.objects.all()
    qry = qry[(page * ROWS_PER_PAGE): ((page + 1) * ROWS_PER_PAGE)]

    users = CustomTable()
    for user in qry:
        users.append([
            user.first_name,
            user.last_name,
            user.email,
        ])
    params['users'] = users

    # data = {
    #     'users': users,
    # }
    return params




class CustomTable(Table):
    headers = ['First Name', 'Last Name', 'Email Address']
    endpoint = '/table/page/'