from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from susanowo.models.tshiryou import TShiryou
from susanowo.forms.shiryouModelForm import TShiryouModelForm
import datetime

# Create your views here.
def shiryouList(request,todo_id):
    shiryou = TShiryouModelForm(request.GET or None)
    # shiryou_list = []
    shiryou_list = TShiryou.objects.filter(todo_id=todo_id).order_by('id')
    # if len(shiryou_list)==0:
    #     shiryou = TShiryou(todo_id=todo_id)
    #     # shiryou_list.add(shiryou)
    #     shiryou_list |= set([shiryou])
    d = {
        'today': datetime.datetime.today().strftime("%Y/%m/%d"),
        'tshiryous': shiryou_list,
        'shiryou': shiryou,
        'todo_id': todo_id,
    }
    # d = {
    #     'today': datetime.datetime.today().strftime("%Y/%m/%d"),
    #     'tshiryous': TShiryou.objects.filter(todo_id=todo_id).order_by('id'),
    #     'shiryou': shiyou,
    # }
    return render(request, 'susanowo/shiryou.html', d)

def shiryouupd(request,todo_id):
    # shiryou_list = TShiryou.objects.filter(todo_id=todo_id).order_by('id')
    # shiryou_list.delete()
    # attach_list = request.POST.getlist('attach')
    # for attach in attach_list:
    #     TShiryou.objects.create(attach = attach, todo_id = todo_id)
    # return redirect('/susanowo/index')
    if request.method == 'POST':
        shiryou_list = TShiryou.objects.filter(todo_id=todo_id).order_by('id')
        shiryou_list.delete()
        attach_list = request.POST.getlist('attach')
        for attach in attach_list:
            TShiryou.objects.create(attach = attach, todo_id = todo_id)
            htmlfile = request.FILES['attach']
            fileobject = FileSystemStorage()
            # filedata = fileobject.save(attach.file.name, attach.file )
            filedata = fileobject.save(htmlfile.name, htmlfile )
            # upload_url = fileobject.url(data)

