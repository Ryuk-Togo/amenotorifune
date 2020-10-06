from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
)
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime, date, timedelta
from django import forms
# import datetime
import logging
import os
from tukuyomi.models.mbuyer import MBuyer
from tukuyomi.forms.buyerForm import BuyerModelForm

def buyer_list(request):
    if request.method == 'GET':
        user_id = request.session.get('LOGIN_USER_ID')
        user_name = request.session.get('LOGIN_USER_NAME')

        mbuyer = MBuyer.objects.filter(user_id=user_id).order_by('buyerNm')

        context = {
            'user_id':user_id,
            'user_name':user_name,
            'form': mbuyer,
            'now_year':datetime.strftime(datetime.now(), '%Y'),
            'now_month':datetime.strftime(datetime.now(), '%m'),
        }

        return render(request, 'tukuyomi/buyer_list.html',context)

def buyer_input(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')

    if request.method == 'GET':
        form = BuyerModelForm(request.GET or None)

        context = {
            'user_id':user_id,
            'user_name':user_name,
            'form': form,
            'shori': '',
            'now_year':datetime.strftime(datetime.now(), '%Y'),
            'now_month':datetime.strftime(datetime.now(), '%m'),
        }
        return render(request, 'tukuyomi/buyer_input.html',context)
    
    elif request.method == 'POST':
        form = BuyerModelForm(request.POST or None)
        if form.is_valid():
            mbuyer = form.save(commit=False)
            mbuyer.user_id = user_id
            mbuyer.create_pg_id   = 'buyer_input'
            mbuyer.create_user_id = user_id
            mbuyer.update_pg_id   = 'buyer_input'
            mbuyer.update_user_id = user_id
            mbuyer.save()
            return redirect('/tukuyomi/buyer_list/')
        else:
            context = {
                'user_id':user_id,
                'user_name':user_name,
                'form': form,
                'shori': '',
                'now_year':datetime.strftime(datetime.now(), '%Y'),
                'now_month':datetime.strftime(datetime.now(), '%m'),
            }
            return render(request, 'tukuyomi/buyer_input.html',context)

def buyer_input_modify(request,id,shori):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')

    if request.method == 'GET':
        mbuyer = MBuyer.objects.get(id=id)
        form = BuyerModelForm(request.GET or None,instance=mbuyer)

        context = {
            'user_id':user_id,
            'user_name':user_name,
            'form': form,
            'shori': shori,
            'id': id,
            'now_year':datetime.strftime(datetime.now(), '%Y'),
            'now_month':datetime.strftime(datetime.now(), '%m'),
        }
        return render(request, 'tukuyomi/buyer_input.html',context)
    
    elif request.method == 'POST':
        form = BuyerModelForm(request.POST)
        if form.is_valid():
            mbuyer = form.save(commit=False)
            mbuyer = get_object_or_404(MBuyer, id=id)
            if shori=='m':
                mbuyer.buyerNm        = request.POST['buyerNm']
                mbuyer.update_date    = timezone.datetime.now()
                mbuyer.update_pg_id   = 'buyer_input'
                mbuyer.update_user_id = user_id
                mbuyer.save()
            elif shori=='d':
                mbuyer.delete()
            return redirect('/tukuyomi/buyer_list/')
        else:
            context = {
                'user_id':user_id,
                'user_name':user_name,
                'form': form,
                'shori':shori,
                'id': id,
                'now_year':datetime.strftime(datetime.now(), '%Y'),
                'now_month':datetime.strftime(datetime.now(), '%m'),
            }
            return render(request, 'tukuyomi/buyer_input.html',context)
