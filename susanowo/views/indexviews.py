from django.shortcuts import render, redirect
from django.http import HttpResponse
from susanowo.models.ttodo import TTodo
import datetime
import json

# Create your views here.
def login(request):
    return HttpResponse('Hello susanowo')

def index(request):
    d = {
        'today': datetime.datetime.today().strftime("%Y/%m/%d"),
        'ttodos': TTodo.objects.order_by('deleted','category','delivery_date'),
    }

    return render(request, 'susanowo/index.html', d)

def modstatus(request):
    if request.method == 'POST':
        id = request.POST.get('param_id')
        complete = request.POST.get('param_complete')
        delete = request.POST.get('param_delete')

        t_todo = TTodo.objects.get(id=id)
        t_todo.completed = complete
        t_todo.deleted = delete
        t_todo.save()

    return HttpResponse(t_todo)
