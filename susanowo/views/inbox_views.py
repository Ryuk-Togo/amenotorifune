from django.shortcuts import render
from django.http import HttpResponse
from susanowo.forms.inboxForm import InboxForm

# Create your views here.
def inbox(request):
    form = InboxForm(request.GET or None)
    d = {
        'form':form,
    }
    return render(request, 'susanowo/inbox.html', d)

def inbox_submit(request):
    d = {
        'title': "",
        'discription': ""
    }
    return render(request, 'susanowo/index.html', d)