from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
)
from django.http import HttpResponse
import datetime
import logging
from django.utils import timezone
from omoikane import const
from omoikane import forms
from omoikane.forms import (
    LoginModelForm, 
    UserInputModelForm, 
    UserModifyModelForm, 
    UserDeleteModelForm,
)
from omoikane.models import MUser, MMenu, MAuth
from django import forms

# Create your views here.
# ログイン画面
def login(request):
    if request.method == 'GET':
        form = LoginModelForm(request.GET or None)
        context = {
            'form': form
        }
        return render(request, 'omoikane/login.html',context)
    elif request.method == 'POST':
        form = LoginModelForm(request.POST)
        if not form.is_valid():
            context = {
                'form': form
            }
            return render(request, 'omoikane/login.html', context)
        return redirect('/omoikane/main/')

def main(request):
    return render(request, 'omoikane/main.html')

def login_input(request):
    if request.method == 'GET':
        form = UserInputModelForm(request.GET or None)
        context = {
            'form': form,
            'shori': '',
            'title': const.SHORI['']
        }
        return render(request, 'omoikane/login_input.html',context)
    elif request.method == 'POST':
        form = UserInputModelForm(request.POST)
        if not form.is_valid():
            context = {
                'form': form,
                'title': const.SHORI['']
            }
            return render(request, 'omoikane/login_input.html', context)
        form.save()
        return redirect('/omoikane/')

def user_list(request):
    if request.method == 'GET':
        musers = MUser.objects.all().order_by('user_name')
        context = {
            'musers': musers
        }
        return render(request, 'omoikane/user_list.html',context)

def user_input_modify(request,user_id,shori):
    if request.method == 'GET':
        muser = MUser.objects.get(user_id=user_id)
        form = UserModifyModelForm(instance=muser)
        context = {
            'form': form,
            'user_id': user_id,
            'shori': shori,
            'title': const.SHORI[shori],
        }
        return render(request, 'omoikane/user_input.html',context)
    elif request.method == 'POST':
        muser = get_object_or_404(MUser, user_id=user_id)
        if shori=='m':
            form = UserModifyModelForm(request.POST)
            if not form.is_valid():
                context = {
                    'form': form,
                    'user_id': user_id,
                    'shori': shori,
                    'title': const.SHORI[shori],
                }
                return render(request, 'omoikane/user_input.html',context)
            
            muser.user_name = form.cleaned_data['user_name']
            if not form.cleaned_data['password1']=='':
                muser.password = form.cleaned_data['password1']
            muser.update_date = timezone.datetime.now()
            muser.update_pg_id = 'omoikane.user_input'
            muser.updaet_user_id = 'admin'
            muser.save()
            return redirect('/omoikane/user_list/')

        elif shori=='d':
            form = UserDeleteModelForm(request.POST)
            if not form.is_valid():
                context = {
                    'form': form,
                    'user_id': user_id,
                    'shori': shori,
                    'title': const.SHORI[shori],
                }
                return render(request, 'omoikane/user_input.html',context)
            
            muser.delete()
            return redirect('/omoikane/user_list/')

def user_input(request):
    if request.method == 'GET':
        form = UserInputModelForm(request.GET or None)
        context = {
            'form': form,
            'shori': '',
            'title': const.SHORI[''],
        }
        return render(request, 'omoikane/user_input.html',context)
    elif request.method == 'POST':
        form = UserInputModelForm(request.POST)
        if not form.is_valid():
            context = {
                'form': form,
                'shori': '',
                'title': const.SHORI[''],
            }
            return render(request, 'omoikane/user_input.html', context)
        form.save()
        return redirect('/omoikane/user_list/')
