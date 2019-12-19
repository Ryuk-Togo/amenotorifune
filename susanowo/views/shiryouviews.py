from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from susanowo.models.tshiryou import TShiryou
from susanowo.forms.shiryouModelForm import TShiryouModelForm, UploadModelFormSet
import datetime

# # Create your views here.
# def shiryouList(request,todo_id):
#     shiryou = TShiryouModelForm(request.GET or None)
#     # shiryou_list = []
#     shiryou_list = TShiryou.objects.filter(todo_id=todo_id).order_by('id')
#     # if len(shiryou_list)==0:
#     #     shiryou = TShiryou(todo_id=todo_id)
#     #     # shiryou_list.add(shiryou)
#     #     shiryou_list |= set([shiryou])
#     d = {
#         'today': datetime.datetime.today().strftime("%Y/%m/%d"),
#         'tshiryous': shiryou_list,
#         'shiryou': shiryou,
#         'todo_id': todo_id,
#     }
#     # d = {
#     #     'today': datetime.datetime.today().strftime("%Y/%m/%d"),
#     #     'tshiryous': TShiryou.objects.filter(todo_id=todo_id).order_by('id'),
#     #     'shiryou': shiyou,
#     # }
#     return render(request, 'susanowo/shiryou.html', d)

# def shiryouupd(request,todo_id):
#     # shiryou_list = TShiryou.objects.filter(todo_id=todo_id).order_by('id')
#     # shiryou_list.delete()
#     # attach_list = request.POST.getlist('attach')
#     # for attach in attach_list:
#     #     TShiryou.objects.create(attach = attach, todo_id = todo_id)
#     # return redirect('/susanowo/index')
#     if request.method == 'POST':
#         shiryou_list = TShiryou.objects.filter(todo_id=todo_id).order_by('id')
#         shiryou_list.delete()
#         attach_list = request.POST.getlist('attach')
#         for attach in attach_list:
#             TShiryou.objects.create(attach = attach, todo_id = todo_id)
#             htmlfile = request.FILES['attach']
#             fileobject = FileSystemStorage()
#             # filedata = fileobject.save(attach.file.name, attach.file )
#             filedata = fileobject.save(htmlfile.name, htmlfile )
#             # upload_url = fileobject.url(data)

# class SingleUploadWithModelView(generic.CreateView):
#     """ファイルモデルのアップロードビュー"""
#     model = TShiryou
#     form_class = TShiryouModelForm
#     template_name = 'susanowo/shiryou.html'
#     success_url = reverse_lazy('susanowo:file_list')

# class FileListView(generic.ListView):
#     """アップロードされたファイルの一覧ページ"""
#     model = TShiryou

# class MultiUploadView(generic.FormView):
#     # form_class = UploadFormSet
#     form_class = UploadModelFormSet
#     template_name = 'susanowo/shiryou.html'

#     def form_valid(self, form):
#         download_url_list = form.save()
#         context = {
#             'download_url_list': download_url_list,
#             'form': form,
#         }
#         return self.render_to_response(context)

def multi_upload_with_model(request,todo_id):
    initial = [{'todo_id':todo_id}]
    formset = UploadModelFormSet(request.POST or None, files=request.FILES or None, queryset=TShiryou.objects.none(), initial=initial)
    if request.method == 'POST':
        if formset.is_valid():
            formset.save()
            # return redirect('susanowo:file_list')
            return redirect('susanowo:index')
        else:
            return HttpResponse("valid false")
    else:
        context = {
            'today': datetime.datetime.today().strftime("%Y/%m/%d"),
            'formset': formset,
            'shiryou': TShiryou.objects.filter(todo_id=todo_id).order_by('id'),
            'todo_id': todo_id,
        }

    return render(request, 'susanowo/shiryou.html', context)

def delete_file(request):
    if request.method == 'POST':
        id = request.POST.get("btnDel")
        todo_id = request.POST.get("todo_id")
        tshiryou = TShiryou.objects.get(id=id)
        if tshiryou is None:
            return HttpResponse("id:" + id)

        else:
            tshiryou.delete()
            return redirect('/susanowo/shiryou/' + todo_id)
