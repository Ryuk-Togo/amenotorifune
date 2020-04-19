from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
)
from django.http import HttpResponse
from django.utils import timezone
from django import forms
from amaterasu.forms import (
    LoginModelForm,
    SiteModelForm,
)
from amaterasu.models import (
    MSite,
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
            return redirect('/amaterasu/menu/')

        form = LoginModelForm(request.GET or None)
        context = {
            'user_id':user_id,
            'user_name':user_name,
            'form': form
        }
        return render(request, 'amaterasu/login.html',context)
    elif request.method == 'POST':
        form = LoginModelForm(request.POST)
        if not form.is_valid():
            context = {
                'form': form
            }
            return render(request, 'amaterasu/login.html', context)
        
        user_id = request.POST['user_id']
        user = MUser.objects.get(user_id=user_id)
        user_name = user.user_name
        request.session['LOGIN_USER_ID'] = user.user_id
        request.session['LOGIN_USER_NAME'] = user.user_name

        context = {
            'user_id':user_id,
            'user_name':user_name,
        }

        # return render(request, 'amaterasu/menu.html', context)
        return redirect('/amaterasu/menu/')

def menu(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        msites = None
        msites = MSite.objects.filter(user_id=user_id).order_by('site_name')
        forms = []
        if msites is not None:
            for msite in msites:
                msite_data = {
                    'id' : msite.id,
                    'site_name' : msite.site_name,
                    'login_user_id' : msite.login_user_id,
                    'login_user_pw' : msite.login_user_pw,
                    'site_url' : msite.site_url,
                }
                forms.append(msite_data)

        context = {
            'user_id':user_id,
            'user_name':user_name,
            'forms': forms,
            'msites': msites,
        }

    return render(request, 'amaterasu/menu.html',context)

def site_input(request,id):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        if id==0:
            form = SiteModelForm()
        else:
            msite = MSite.objects.get(id=id)
            initialize = {
                'id':id,
                'user_id':user_id,
                'site_name':msite.site_name,
                'login_user_id':msite.login_user_id,
                'login_user_pw':msite.login_user_pw,
                're_login_user_pw':msite.login_user_pw,
                'site_url':msite.site_url,
            }
            form = SiteModelForm(initial=initialize)
        context = {
            'user_id':user_id,
            'user_name':user_name,
            'form': form,
            'id': id,
        }
        return render(request, 'amaterasu/site_input.html',context)
    
    elif request.method == 'POST':
        form = SiteModelForm(request.POST or None)
        try:
            msite = get_object_or_404(MSite, pk=id)
        except:
            msite = None
        
        if 'btn_input' in request.POST:
            if form.is_valid():

                if msite is None:
                    msite = MSite()
                    msite.create_date    = timezone.datetime.now()
                    msite.create_pg_id   = 'amaterasu.site_input'
                    msite.create_user_id = user_id

                msite.user_id        = user_id
                msite.site_name      = request.POST['site_name']
                msite.login_user_id  = request.POST['login_user_id']
                msite.login_user_pw  = request.POST['login_user_pw']
                msite.site_url       = request.POST['site_url']
                msite.update_date    = timezone.datetime.now()
                msite.update_pg_id   = 'amaterasu.site_input'
                msite.updaet_user_id = user_id
                msite.save()

            else:
                context = {
                    'user_id':user_id,
                    'user_name':user_name,
                    'form': form,
                    'id': id,
                }
                return render(request, 'amaterasu/site_input.html',context)
        elif 'btn_delete' in request.POST:
            if msite is not None:
                msite.delete()
    
        return redirect('/amaterasu/menu/')
