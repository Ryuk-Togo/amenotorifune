from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
)
from django.http import HttpResponse
from django.utils import timezone
from django import forms
from amenouzume.forms import (
    LoginModelForm,
    PlaceModelForm,
    PlaceDeleteModelForm,
    ItemModelForm,
    ItemDeleteModelForm,
)
from amenouzume.models import (
    MPlace,
    MItem,
    MItemPlace,
    TStock,
    TStockHistory
)
from omoikane.models import (
    MUser,
)
import datetime
import logging
import os
from izanagi import settings

# Create your views here.
# ログイン画面
def login(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        if not (user_id is None and user_name is None):
            return redirect('/amenouzume/menu/')

        form = LoginModelForm(request.GET or None)
        context = {
            'user_id':user_id,
            'user_name':user_name,
            'form': form
        }
        return render(request, 'amenouzume/login.html',context)
    elif request.method == 'POST':
        form = LoginModelForm(request.POST)
        if not form.is_valid():
            context = {
                'form': form
            }
            return render(request, 'amenouzume/login.html', context)
        
        user_id = request.POST['user_id']
        user = MUser.objects.get(user_id=user_id)
        user_name = user.user_name
        request.session['LOGIN_USER_ID'] = user.user_id
        request.session['LOGIN_USER_NAME'] = user.user_name

        context = {
            'user_id':user_id,
            'user_name':user_name,
        }

        return redirect('/amenouzume/menu/')
        # return render(request, 'amenouzume/menu.html',context)

def menu(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        context = {
            'user_id':user_id,
            'user_name':user_name,
        }

    return render(request, 'amenouzume/menu.html',context)

def place(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        mplaces = MPlace.objects.filter(user_id=user_id).order_by('place_name')
        context = {
            'user_id':user_id,
            'user_name':user_name,
            'forms':mplaces
        }
    elif request.method == 'POST':
        return redirect('/amenouzume/place_input/')
        
    return render(request, 'amenouzume/place.html',context)

def place_input(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        form = PlaceModelForm()
        context = {
            'user_id':user_id,
            'user_name':user_name,
            'form': form,
            'shori': '',
        }
        return render(request, 'amenouzume/place_input.html',context)
    elif request.method == 'POST':
        form = PlaceModelForm(request.POST)
        if not form.is_valid():
            context = {
                'user_id':user_id,
                'user_name':user_name,
                'form': form,
                'shori': '',
            }
            return render(request, 'amenouzume/place_input.html', context)
        mplace = form.save(commit=False)
        mplace.user_id        = user_id
        mplace.place_name     = form.cleaned_data['place_name']
        mplace.create_pg_id   = 'amenouzume.place_input'
        mplace.create_user_id = user_id
        mplace.update_pg_id   = 'amenouzume.place_input'
        mplace.update_user_id = user_id
        mplace.save()

        return redirect('/amenouzume/place/')
    
def place_input_modify(request, id, shori):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        mplace = MPlace.objects.get(id=id)
        form = PlaceModelForm(instance=mplace)
        context = {
            'user_id': user_id,
            'user_name':user_name,
            'form': form,
            'id': id,
            'shori': shori,
        }
        return render(request, 'amenouzume/place_input.html',context)
    elif request.method == 'POST':
        mplace = get_object_or_404(MPlace, id=id)
        if shori=='m':
            form = PlaceModelForm(request.POST)
            if not form.is_valid():
                context = {
                    'user_id': user_id,
                    'user_name':user_name,
                    'form': form,
                    'id': id,
                    'shori': shori,
                }
                return render(request, 'amenouzume/place_input.html',context)
            
            mplace.place_name = form.cleaned_data['place_name']
            mplace.update_date = timezone.datetime.now()
            mplace.update_pg_id = 'amenouzume.place_input'
            mplace.updaet_user_id = user_id
            mplace.save()
            return redirect('/amenouzume/place/')

        elif shori=='d':
            form = PlaceDeleteModelForm(request.POST)
            if not form.is_valid():
                context = {
                    'form': form,
                    'user_id': user_id,
                    'user_name':user_name,
                    'id': id,
                    'shori': shori,
                }
                return render(request, 'amenouzume/place_input.html',context)
            
            mplace.delete()
            return redirect('/amenouzume/place/')
    
def item(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        mitems = MItem.objects.filter(user_id=user_id).order_by('item_name')
        context = {
            'user_id':user_id,
            'user_name':user_name,
            'forms':mitems
        }
    elif request.method == 'POST':
        return redirect('/amenouzume/item_input/')
        
    return render(request, 'amenouzume/item.html',context)

def item_input(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        form = ItemModelForm()
        context = {
            'user_id':user_id,
            'user_name':user_name,
            'form': form,
            'shori': '',
        }
        return render(request, 'amenouzume/item_input.html',context)
    elif request.method == 'POST':
        form = ItemModelForm(request.POST)
        if not form.is_valid():
            context = {
                'user_id':user_id,
                'user_name':user_name,
                'form': form,
                'shori': '',
            }
            return render(request, 'amenouzume/item_input.html', context)
        mitem = form.save(commit=False)
        mitem.user_id        = user_id
        mitem.item_name      = form.cleaned_data['item_name']
        mitem.safety_amt     = form.cleaned_data['safety_amt']
        mitem.item_term      = form.cleaned_data['item_term']
        mitem.create_pg_id   = 'amenouzume.item_input'
        mitem.create_user_id = user_id
        mitem.update_pg_id   = 'amenouzume.item_input'
        mitem.update_user_id = user_id
        mitem.save()

        return redirect('/amenouzume/item/')
    
def item_input_modify(request, id, shori):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        mitem = MItem.objects.get(id=id)
        if shori=='m':
            form = ItemModelForm(instance=mitem)
        else:
            form = ItemDeleteModelForm(instance=mitem)
        
        context = {
            'user_id': user_id,
            'user_name':user_name,
            'form': form,
            'id': id,
            'shori': shori,
        }
        return render(request, 'amenouzume/item_input.html',context)
    elif request.method == 'POST':
        mitem = get_object_or_404(MItem, id=id)
        if shori=='m':
            form = ItemModelForm(request.POST)
            if not form.is_valid():
                context = {
                    'user_id': user_id,
                    'user_name':user_name,
                    'form': form,
                    'id': id,
                    'shori': shori,
                }
                return render(request, 'amenouzume/item_input.html',context)
            
            mitem.item_name      = form.cleaned_data['item_name']
            mitem.safety_amt     = form.cleaned_data['safety_amt']
            mitem.item_term      = form.cleaned_data['item_term']
            mitem.update_date    = timezone.datetime.now()
            mitem.update_pg_id   = 'amenouzume.item_input'
            mitem.updaet_user_id = user_id
            mitem.save()
            return redirect('/amenouzume/item/')

        elif shori=='d':
            form = ItemDeleteModelForm(request.POST)
            if not form.is_valid():
                context = {
                    'form': form,
                    'user_id': user_id,
                    'user_name':user_name,
                    'id': id,
                    'shori': shori,
                }
                return render(request, 'amenouzume/item_input.html',context)
            
            mitem.delete()
            return redirect('/amenouzume/item/')

def place_item(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        context = {
            'user_id':user_id,
            'user_name':user_name,
        }

    return render(request, 'amenouzume/menu.html',context)

def stock_data(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        context = {
            'user_id':user_id,
            'user_name':user_name,
        }

    return render(request, 'amenouzume/menu.html',context)

def stock_data_history(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        context = {
            'user_id':user_id,
            'user_name':user_name,
        }

    return render(request, 'amenouzume/menu.html',context)

