from django.shortcuts import render, redirect
from django.http import HttpResponse
from susanowo.forms.inboxModelForm import InboxModelForm
import datetime
# from susanowo.forms.inboxForm import InboxForm
# from susanowo.models.ttodo import TTodo

# Create your views here.
def inbox(request):
    form = InboxModelForm(request.GET or None)
    # form = InboxModelForm{user_id="admin")
    d = {
        'form':form,
    }
    return render(request, 'susanowo/inbox.html', d)

def inboxupd(request):
    mForm = InboxModelForm(request.POST)
    if mForm.is_valid():
        mForm.save()
        # ttodo = mForm.save(commit=True)
        # ttodo.save()
        d = {
            'today': datetime.datetime.today().strftime("%Y/%m/%d"),
        }
        return render(request, 'susanowo/index.html', d)
    else:
        d = {
            'form':mForm
        }
    return render(request, 'susanowo/indox.html')
