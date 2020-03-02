from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
)
from django.http import HttpResponse
from django.utils import timezone
from django import forms
import datetime
import logging
import os
from izanagi import settings
from tukuyomi.forms.loginForm import LoginModelForm
from omoikane.models import MUser

def login(request):
    if request.method == 'GET':
        user_id = request.session.get('LOGIN_USER_ID')
        user_name = request.session.get('LOGIN_USER_NAME')
        form = LoginModelForm(request.GET or None)
        context = {
            'form': form
        }

        if user_id:
            return redirect('/tukuyomi/menu/')

        return render(request, 'tukuyomi/login.html',context)

    elif request.method == 'POST':
        user_id = request.session.get('LOGIN_USER_ID')
        user_name = request.session.get('LOGIN_USER_NAME')
        if user_id is None:
            user_id = request.POST['user_id']
            user = MUser.objects.get(user_id=user_id)
            user_name = user.user_name
            request.session['LOGIN_USER_ID'] = user.user_id
            request.session['LOGIN_USER_NAME'] = user.user_name

        form = LoginModelForm(request.POST)
        if form.is_valid():
            return redirect('/tukuyomi/menu/')
        else:
            context = {
                'user_id': user_id,
                'user_name': user_name,
                'form': form,
            }
            return render(request, 'tukuyomi/login.html', context)
