from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
)
from django.http import HttpResponse
from django.utils import timezone
from django import forms
from django.db import connection
from datetime import datetime, date, timedelta
import logging
import os
from tukuyomi.models.tshiharaih import TShiharaiH
from tukuyomi.models.massert import MAssert
from tukuyomi.forms.shiharaihForm import TShiharaiHModelForm, TShiharaiHDeleteModelForm

def shiharaih_input(request, assert_cd):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    massert = MAssert.objects.get(id=assert_cd)

    if request.method == 'GET':
        form = TShiharaiHModelForm(request.GET or None)

        context = {
            'user_id':user_id,
            'user_name':user_name,
            'assert_cd':assert_cd,
            'assert_nm':massert.assert_nm,
            'form': form,
            'shori': '',
        }
        return render(request, 'tukuyomi/shiharaih_input.html',context)
    
    elif request.method == 'POST':
        form = TShiharaiHModelForm(request.POST or None)
        if form.is_valid():
            tshiharaih                = form.save(commit=False)
            tshiharaih.user_id        = user_id
            tshiharaih.assert_cd      = assert_cd
            tshiharaih.create_pg_id   = 'assert_input'
            tshiharaih.create_user_id = user_id
            tshiharaih.update_pg_id   = 'assert_input'
            tshiharaih.update_user_id = user_id
            tshiharaih.save()
            used_year = datetime.strftime(tshiharaih.used_date, '%Y')
            used_month = datetime.strftime(tshiharaih.used_date, '%m')
            return redirect('/tukuyomi/riyou_info/' + used_year + '/' + used_month)
        else:
            # form.fields['assert_nm'].choices = get_assert_combo(user_id)
            context = {
                'user_id':user_id,
                'user_name':user_name,
                'assert_cd':assert_cd,
                'assert_nm':massert.assert_nm,
                'form': form,
                'shori': '',
            }
            return render(request, 'tukuyomi/shiharaih_input.html',context)
        
    return HttpResponse('shiharaih_input_init')

def shiharaih_input_modify(request,shiharaih_id,shori):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')

    if request.method == 'GET':
        tshiharaih = TShiharaiH.objects.get(id=shiharaih_id)
        massert = MAssert.objects.get(id=tshiharaih.assert_cd)
        form = None
        if shori=='m':
            form = TShiharaiHModelForm(request.GET or None,instance=tshiharaih)
        else:
            form = TShiharaiHDeleteModelForm(request.GET or None,instance=tshiharaih)

        context = {
            'user_id':user_id,
            'user_name':user_name,
            'assert_cd':massert.id,
            'assert_nm':massert.assert_nm,
            'form': form,
            'shiharaih_id': shiharaih_id,
            'shori': shori,
        }
        return render(request, 'tukuyomi/shiharaih_input.html',context)
    
    elif request.method == 'POST':
        form = TShiharaiHModelForm(request.POST)
        if form.is_valid():
            tshiharaih = form.save(commit=False)
            tshiharaih = get_object_or_404(TShiharaiH, id=shiharaih_id)
            used_year = datetime.strftime(tshiharaih.used_date, '%Y')
            used_month = datetime.strftime(tshiharaih.used_date, '%m')
            # massert = MAssert.objects.get(id=tshiharaih.assert_cd)

            if shori=='m':
                tshiharaih.used_date      = request.POST['used_date']
                tshiharaih.shop_name      = request.POST['shop_name']
                tshiharaih.used_amt       = request.POST['used_amt']
                tshiharaih.receipt        = request.POST['receipt']
                tshiharaih.update_date    = timezone.datetime.now()
                tshiharaih.update_pg_id   = 'shiharaih_input'
                tshiharaih.update_user_id = user_id
                tshiharaih.save()
            elif shori=='d':
                tshiharaih.delete()

            # context = {
            #     'user_id':user_id,
            #     'user_name':user_name,
            #     'assert_cd': massert.id,
            #     'assert_nm': massert.assert_nm,
            #     'used_year': used_year,
            #     'used_month': used_month,
            #     'form': form,
            # }

            # return render(request, 'tukuyomi/shiharai_info.html',context)
            # return HttpResponse('/tukuyomi/shiharai_info/' + used_year + '/' + used_month + '/' + str(tshiharaih.assert_cd))
            return redirect('/tukuyomi/shiharai_info/' + used_year + '/' + used_month + '/' + str(tshiharaih.assert_cd))
        else:
            context = {
                'user_id':user_id,
                'user_name':user_name,
                'assert_cd':massert.id,
                'assert_nm':massert.assert_nm,
                'form': form,
                'shiharaih_id': shiharaih_id,
                'shori':shori,
            }
            return render(request, 'tukuyomi/shiharaih_input.html',context)
