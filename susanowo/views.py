from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def login(request):
    return HttpResponse('Hello susanowo')

def index(request):
    d = {
        'today': datetime.datetime.today().strftime("%Y/%m/%d/")
    }
    return render(request, 'susanowo/index.html', d)

def inbox(request):
    return render(request, 'susanowo/inbox.html')