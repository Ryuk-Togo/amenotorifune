from django.shortcuts import render
from django.http import HttpResponse
from susanowo.forms.inboxForm import InboxForm
# from susanowo.models.ttodo import TTodo

# Create your views here.
def inbox(request):
    form = InboxForm(request.GET or None)
    d = {
        'form':form,
    }
    return render(request, 'susanowo/inbox.html', d)

def inbox_submit(request):
    form = InboxForm(request.POST)
    # t_todo = InboxModelForm()
    if form.is_valid():
        # t_todo.object.create(**form.cleaned_data)
        form.save();
        return redirect('t_todo:t_todo_models')
    d = {
        'form': form
    }
    return render(request, 'susanowo/index.html', d)