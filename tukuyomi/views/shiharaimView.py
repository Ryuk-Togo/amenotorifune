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
from tukuyomi.models.tshiharaim import TShiharaiM
from tukuyomi.models.massert import MAssert
from tukuyomi.models.mbuyer import MBuyer
from tukuyomi.forms.shiharaimForm import TShiharaiMModelForm, TShiharaiMModelFormSet

def shiharaim_input(request, assert_cd,y,m,d,shop_name):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    used_date = datetime(year=y,month=m,day=d)

    if request.method == 'GET':

        buyer_choice = get_buyer_list(user_id)

        tshiharaims = TShiharaiM.objects.filter(user_id=user_id).filter(assert_cd=assert_cd).filter(shop_name=shop_name).filter(used_date=used_date)
        initial_data = []
        shiharai_row = 0
        for shiharaim in tshiharaims:
            shiharai_row += 1
            initial_data.append(
                {
                    'id' : shiharaim.id,
                    'item_nm' : shiharaim.item_nm,
                    'buyer_cd' : shiharaim.buyer_cd,
                    'sum_user_amt' : shiharaim.sum_user_amt,
                    # 'buyer_choice' : buyer_choice,
                    'shiharai_row' : shiharai_row,
                }
            )
        
        shiharai_row += 1
        initial_data.append(
            {
                'id' : None,
                'item_nm' : '',
                'buyer_cd' : '',
                'sum_user_amt' : None,
                # 'buyer_choice' : buyer_choice,
                'shiharai_row' : shiharai_row,
            }
        )

        formset = TShiharaiMModelFormSet(request.GET or None, initial=initial_data)
        for form in formset:
            form.fields['buyer_choice'].choices = buyer_choice

        context = {
            'user_id': user_id,
            'user_name': user_name,
            'y': y,
            'm': m,
            'd': d,
            'shop_name': shop_name,
            'assert_cd': assert_cd,
            'formset': formset,
            'shiharai_row' : shiharai_row,
        }
        return render(request, 'tukuyomi/shiharaim_input.html',context)
    
    elif request.method == 'POST':
        formset = TShiharaiMModelFormSet(request.POST)
        now_datetime = timezone.datetime.now()
        if formset.is_valid():
            instances = formset.save(commit=False)
            for form in instances:
                if form.is_valid():
                    tshiharaim = form.save(commit=False)
            return redirect('/tukuyomi/shiharai_info/' + str(y) + '/' + str(m) + '/' + str(assert_cd))

        context = {
            'user_id': user_id,
            'user_name': user_name,
            'y': y,
            'm': m,
            'd': d,
            'shop_name': shop_name,
            'assert_cd': assert_cd,
            'formset': formset,
            'shiharai_row' : 1,
        }
        return render(request, 'tukuyomi/shiharaim_input.html',context)
        
        # else:
        #     instances = formset.save(commit=False)
        #     for form in instances:
        #         if form.is_valid():
        #             pass
        #         else:
        #             form.save(commit=False)
        #         tshiharaim = form.save(commit=False)
        #         if tshiharaim.id is None:
        #             # 新規挿入
        #             tshiharaim.user_id = user_id
        #             tshiharaim.used_date = datetime(year=y,month=m,day=d)
        #             tshiharaim.shop_name = shop_name
        #             tshiharaim.assert_cd = assert_cd
        #             tshiharaim.refund_balance = 0
        #             tshiharaim.create_pg_id   = 'assert_input'
        #             tshiharaim.create_user_id = user_id
        #             tshiharaim.create_date    = now_datetime
        #             tshiharaim.update_pg_id   = 'assert_input'
        #             tshiharaim.update_user_id = user_id
        #             tshiharaim.update_date    = now_datetime
        #             tshiharaim.save()
        #         else:
        #             # 更新
        #             tshiharaim.update_pg_id   = 'assert_input'
        #             tshiharaim.update_user_id = user_id
        #             tshiharaim.update_date    = now_datetime
        #             tshiharaim.save()

        # tshiharaim_del = get_object_or_404(TShiharaiM, update_date=now_datetime)
        # tshiharaim_del.delete()

        # context = {
        #     'user_id': user_id,
        #     'user_name': user_name,
        #     'y': y,
        #     'm': m,
        #     'd': d,
        #     'assert_cd': assert_cd,
        # }
        # return redirect('/tukuyomi/shiharai_info/' + str(y) + '/' + str(m) + '/' + str(assert_cd))

def get_buyer_list(user_id):
    mbuyers = MBuyer.objects.filter(user_id=user_id).order_by('buyerNm')
    buyer_choice = []
    buyer_choice.append(('', ''))
    for buyer in mbuyers:
        buyer_choice.append((buyer.id, buyer.buyerNm))
    return buyer_choice
