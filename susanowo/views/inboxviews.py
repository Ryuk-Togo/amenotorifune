from django.shortcuts import render, redirect
from django.http import HttpResponse
from susanowo.forms.inboxModelForm import InboxModelForm
# from susanowo.forms.inboxForm import InboxForm
# from susanowo.models.ttodo import TTodo

# Create your views here.
def inbox(request):
    form = InboxModelForm(request.GET or None)
    d = {
        'message' : '',
        'form':form,
    }
    return render(request, 'susanowo/inbox.html', d)

def inbox_submit(request):
    mForm = InboxModelForm(request.POST)
    if mForm.is_valid():
        ttodo = mForm.save(commit=True)
        ttodo.save()
        return render(request, 'susanowo/index.html')

    d = {
        'message' : 'エラー発生',
        'form': mForm,
    }
    return render(request, 'susanowo/indox.html', d)
