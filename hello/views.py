from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
# import requests
# Create your views here.
def index(request):
    # return HttpResponse('<h1>Chend Blog</h1>')
    return render(request, 'index.html')
    # r = requests.get('<h1> Chend Blog <h1>')
    # print(r.text)
    # return HttpResponse('<pre>' + r.text + '</pre>')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

