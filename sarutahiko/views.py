from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
)
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from sarutahiko.forms import (
    LoginModelForm,
)
# from sarutahiko.models import (
# )
from amenouzume.models import (
    MItem,
)
from omoikane.models import (
    MUser,
)
import datetime
import logging
import os
from izanagi import settings
from django.forms import formsets
import json
from django.http.response import JsonResponse

# Create your views here.
# ログイン画面
def login(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        if not (user_id is None and user_name is None):
            year = timezone.strftime('%Y')
            month = timezone.strftime('%m')
            return redirect('/sarutahiko/calendar%year=' + year + '&month=' + month)

        form = LoginModelForm(request.GET or None)
        context = {
            'user_id':user_id,
            'user_name':user_name,
            'form': form
        }
        return render(request, 'sarutahiko/login.html',context)
    elif request.method == 'POST':
        form = LoginModelForm(request.POST)
        if not form.is_valid():
            context = {
                'form': form
            }
            return render(request, 'sarutahiko/login.html', context)
        
        user_id = request.POST['user_id']
        user = MUser.objects.get(user_id=user_id)
        user_name = user.user_name
        request.session['LOGIN_USER_ID'] = user.user_id
        request.session['LOGIN_USER_NAME'] = user.user_name

        context = {
            'user_id':user_id,
            'user_name':user_name,
        }

        return redirect('/sarutahiko/calendar/')
        # return render(request, 'amenouzume/menu.html',context)

def menu(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        context = {
            'user_id':user_id,
            'user_name':user_name,
        }

    return render(request, 'sarutahiko/menu.html',context)

def recipe(request):
    return render(request, 'sarutahiko/recipe.html',context)

def calendar(request, year, month):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':

        context = {
            'user_id':user_id,
            'user_name':user_name,
        }

        return render(request, 'sarutahiko/calendar.html',context)

def kondate(request):
    return render(request, 'sarutahiko/kondate.html',context)

def item(request):
    return render(request, 'sarutahiko/item.html',context)

def send(request):
    return render(request, 'sarutahiko/send.html',context)
