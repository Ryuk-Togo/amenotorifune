from django.shortcuts import render, redirect
from django.http import HttpResponse
from susanowo.models.ttodo import TTodo
import datetime

# Create your views here.
def login(request):
    return HttpResponse('Hello susanowo')

def index(request):
    d = {
        'today': datetime.datetime.today().strftime("%Y/%m/%d"),
        'ttodos': TTodo.objects.filter(deleted=False).order_by('category','delivery_date'),
    }
    
    return render(request, 'susanowo/index.html', d)

def complete(request):
    if request.POST == 'POST':
        id = request.POST['id']
        value = request.POST['value']
        mForm = TTodo.objects.filter(id=id)
        mForm.completed = value
        if mForm.is_valid():
            mForm.save()

    return redirect('/susanowo/index')

