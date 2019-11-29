from django.shortcuts import (
    render, 
    redirect, 
    get_object_or_404,
)
from django.http import HttpResponse
from susanowo.forms.inboxModelForm import InboxModelForm
from susanowo.models import ttodo
from susanowo.models.ttodo import TTodo
import datetime
import logging
# from susanowo.forms.inboxForm import InboxForm
# from susanowo.models.ttodo import TTodo

# Create your views here.
def inbox(request,todo_id):
    form = InboxModelForm(request.GET or None)
    # form = InboxModelForm{user_id="admin")
    if todo_id is not None :
        # id = request.GET.get("rownum")
        t_todo = TTodo.objects.get(id=todo_id)
        form = InboxModelForm(instance=t_todo)
    d = {
        'form':form,
        'todo_id':todo_id,
    }
    return render(request, 'susanowo/inbox.html', d)

def newInbox(request):
    form = InboxModelForm(request.GET or None)
    d = {
        'form':form,
        'todo_id':'',
    }
    return render(request, 'susanowo/inbox.html', d)

def inboxUpd(request,todo_id):
    todo = get_object_or_404(TTodo,id=todo_id)
    form = InboxModelForm(request.POST)
    if form.is_valid():
        todo.title             = form.cleaned_data['title']
        todo.discription       = form.cleaned_data['discription']
        todo.should_action     = form.cleaned_data['should_action']
        todo.action_selection  = form.cleaned_data['action_selection']
        todo.delivery_date     = form.cleaned_data['delivery_date']
        todo.single_action     = form.cleaned_data['single_action']
        todo.can_do_tow_minite = form.cleaned_data['can_do_tow_minite']
        todo.should_myself     = form.cleaned_data['should_myself']
        todo.should_do_oneday  = form.cleaned_data['should_do_oneday']
        todo.date_should_do    = form.cleaned_data['date_should_do']
        todo.request_pertner   = form.cleaned_data['request_pertner']
        todo.category          = ttodo.computeCategory(todo)
        todo.save()
        return redirect('/susanowo/index')
    else:
        d = {
            'form':form,
            'todo_id':todo_id,
        }
    return render(request, 'susanowo/indox.html', d)

def inboxAdd(request):
    mForm = InboxModelForm(request.POST)
    if mForm.is_valid():
        todo = mForm.save()
        todo.category = ttodo.computeCategory(todo)
        todo.save()
        return redirect('/susanowo/index')
    else:
        d = {
            'form':mForm,
            'todo_id':'',
        }
    return render(request, 'susanowo/indox.html', d)
