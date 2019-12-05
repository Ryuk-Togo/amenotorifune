from django.shortcuts import render, redirect
from django.http import HttpResponse
from susanowo.models.ttodo import TTodo
from susanowo.forms.inboxModelForm import InboxModelForm
import datetime

# Create your views here.
def gomibakoList(request):
    d = {
        'today': datetime.datetime.today().strftime("%Y/%m/%d"),
        'ttodos': TTodo.objects.filter(category='08').order_by('create_date'),
    }
    return render(request, 'susanowo/gomibako.html', d)

def gomiSakujo(request):
    # delete_list = request.POST.getlist()
    # delete_list = request.POST.lists()
    deleted_list = request.POST.getlist('deleted')
    # id_list = request.POST.getlist('id')
    for id in deleted_list:
        t_todo = TTodo.objects.get(id=id)
        t_todo.delete()

    return redirect('/susanowo/index')
