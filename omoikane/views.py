from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
)
from django.http import HttpResponse
from django.utils import timezone
from django import forms
from omoikane import const
from omoikane import forms
from omoikane.forms import (
    LoginModelForm, 
    UserInputModelForm, 
    UserModifyModelForm, 
    UserDeleteModelForm,
    MenuInputModelForm,
    MenuModifyModelForm,
    MenuDeleteModelForm,
)
from omoikane.models import (
    MUser,
    MMenu,
    MAuth,
)
import datetime
import logging
import os
from izanagi import settings

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
            'title': const.USER_SHORI['']
        }
        return render(request, 'omoikane/login_input.html',context)
    elif request.method == 'POST':
        form = UserInputModelForm(request.POST)
        if not form.is_valid():
            context = {
                'form': form,
                'title': const.USER_SHORI['']
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
            'title': const.USER_SHORI[shori],
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
                    'title': const.USER_SHORI[shori],
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
                    'title': const.USER_SHORI[shori],
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
            'title': const.USER_SHORI[''],
        }
        return render(request, 'omoikane/user_input.html',context)
    elif request.method == 'POST':
        form = UserInputModelForm(request.POST)
        if not form.is_valid():
            context = {
                'form': form,
                'shori': '',
                'title': const.USER_SHORI[''],
            }
            return render(request, 'omoikane/user_input.html', context)
        form.save()
        return redirect('/omoikane/user_list/')

def menu_list(request):
    if request.method == 'GET':
        mmenus = MMenu.objects.all().order_by('id')
        context = {
            'mmenus': mmenus
        }
        return render(request, 'omoikane/menu_list.html',context)

def menu_input(request):
    if request.method == 'GET':
        form = MenuInputModelForm(request.GET or None)
        context = {
            'form': form,
            'shori': '',
            'title': const.MENU_SHORI[''],
        }
        return render(request, 'omoikane/menu_input.html',context)
    elif request.method == 'POST':
        form = MenuInputModelForm(request.POST)
        if not form.is_valid():
            context = {
                'form': form,
                'shori': '',
                'title': const.MENU_SHORI[''],
            }
            return render(request, 'omoikane/menu_input.html', context)
        mmenu = MMenu()
        mmenu.menu_name = request.POST['menu_name']
        mmenu.url = request.POST['url']
        mmenu.icon = request.FILES['icon']
        mmenu.create_date = timezone.datetime.now()
        mmenu.create_pg_id = 'omoikane.update_input'
        mmenu.create_user_id = 'admin'
        mmenu.update_date = timezone.datetime.now()
        mmenu.update_pg_id = 'omoikane.update_input'
        mmenu.updaet_user_id = 'admin'
        mmenu.save()
        return redirect('/omoikane/menu_list/')

def menu_input_modify(request,id,shori):
    if request.method == 'GET':
        mmenu = MMenu.objects.get(pk=id)
        initialize = {
            'menu_id':id,
            'menu_name':mmenu.menu_name,
            'url':mmenu.url,
            'icon':mmenu.icon,
        }
        form = MenuModifyModelForm(initial=initialize)
        context = {
            'form': form,
            'id': id,
            'shori': shori,
            'title': const.MENU_SHORI[shori],
        }
        return render(request, 'omoikane/menu_input.html',context)
    elif request.method == 'POST':
        mmenu = get_object_or_404(MMenu, pk=id)
        # imagePath = mmenu.icon
        if shori=='m':
            form = MenuModifyModelForm(request.POST, files=request.FILES or None)
            if not form.is_valid():
                context = {
                    'form': form,
                    'id': id,
                    'shori': shori,
                    'title': const.MENU_SHORI[shori],
                }
                return render(request, 'omoikane/menu_input.html',context)

            # mmenu.id = form.cleaned_data['menu_id']
            # mmenu.menu_name = form.cleaned_data['menu_name']
            # mmenu.url = form.cleaned_data['url']
            # mmenu.icon = form.cleaned_data['icon']

            mmenu.id = request.POST['menu_id']
            mmenu.menu_name = request.POST['menu_name']
            mmenu.url = request.POST['url']
            # if form.cleaned_data['icon'] is None or form.cleaned_data['icon']=='':
            # if request.FILES['icon'] is None or request.FILES['icon']=='':
            #     pass
            # else:
            #     mmenu.icon = request.FILES['icon']
            mmenu.icon = request.FILES['icon']
            mmenu.update_date = timezone.datetime.now()
            mmenu.update_pg_id = 'omoikane.update_input'
            mmenu.updaet_user_id = 'admin'
            # if imagePath:
            #     os.remove(settings.MEDIA_ROOT + '/' + imagePath)
            mmenu.save()
            return redirect('/omoikane/menu_list/')

        elif shori=='d':
            form = MenuDeleteModelForm(request.POST)
            if not form.is_valid():
                context = {
                    'form': form,
                    'id': id,
                    'shori': shori,
                    'title': const.MENU_SHORI[shori],
                }
                return render(request, 'omoikane/menu_input.html',context)
            
            # if imagePath:
            #     os.remove(settings.MEDIA_ROOT + '/' + imagePath)
            mmenu.delete()
            return redirect('/omoikane/menu_list/')

