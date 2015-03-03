import datetime

from django.template import Context, loader
from django.http import HttpResponse
from django import forms
from homepage import models as hmod
from lib.customform import CustomForm
from lib.widgets import DatePickWidget


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
    images = hmod.GalleryImage.objects.all()
    t = l.get_template('gallery.html')
    c = Context({
        'images': images,
    })

    return HttpResponse(t.render(c))