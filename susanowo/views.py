from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return HttpResponse('Hello susanowo')

def index(request):
    return render(request, 'susanowo/index.html')
