from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from susanowo.models.ttodo import TTodo
from susanowo.forms.loginModelForm import MUserModelForm
from omoikane.models import MUser
import datetime

# Create your views here.
def login(request):
    if request.method == 'GET':
        form = MUserModelForm(request.GET or None)
        context = {
            'form': form
        }
        return render(request, 'susanowo/login.html', context)
    else:
        form = MUserModelForm(request.POST)
        if not form.is_valid():
            context = {
                'form': form
            }
            return render(request, 'susanowo/login.html', context)
        return redirect('/susanowo/index')

def requestLogin(request):

    return HttpResponse('Hello susanowo')

def index(request):
    d = {
        'today': datetime.datetime.today().strftime("%Y/%m/%d"),
        'ttodos': TTodo.objects.filter(~Q(category='07') & ~Q(category='08')).order_by('deleted','category','delivery_date'),
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
