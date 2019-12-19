from django import forms
from django.db import models
from susanowo.models.tshiryou import TShiryou
from django.core.files.storage import default_storage

# class SingleUploadForm(forms.Form):
#     file = forms.ImageField(label='画像ファイル')

#     def save(self):
#         upload_file = self.cleaned_data['file']
#         file_name = default_storage.save(upload_file.name, upload_file)
#         return default_storage.url(file_name)

class TShiryouModelForm(forms.ModelForm):
    class Meta:
        model = TShiryou
        fields = ('todo_id','attach')
        # fields = '__all__'
        widgets = {
            'todo_id': forms.HiddenInput(),
        }

# class BaseUploadFormSet(forms.BaseFormSet):
#     def save(self):
#         # ['/media/1.png', '/media/2.png']のようなファイルのURLが入ったリストになる
#         url_list = []

#         # SingleUploadFormのsaveを順に呼び出し、ファイルURLを集める
#         for form in self.forms:
#             try:
#                 url = form.save()
#             except KeyError:
#                 # ファイルがアップロードされていないフォームは、KeyErrorになるので、ここで無視する
#                 pass
#             else:
#                 url_list.append(url)
#         return url_list

UploadModelFormSet = forms.modelformset_factory(
    TShiryou, form=TShiryouModelForm,
    extra=1
)

# UploadFormSet = forms.formset_factory(
#     TShiryouModelForm, formset=BaseUploadFormSet, 
#     extra=1
# )