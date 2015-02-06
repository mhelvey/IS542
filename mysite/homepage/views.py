from django.shortcuts import render
from django.shortcuts import render_to_response
import requests

# Create your views here.
def base(request):
    return render_to_response('base.html')