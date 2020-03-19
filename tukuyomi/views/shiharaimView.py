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
    shiharai_row = 0
    used_year = datetime.strftime(used_date, '%Y')
    used_month = datetime.strftime(used_date, '%m')
    used_day = datetime.strftime(used_date, '%d')

    if request.method == 'GET':

        tshiharaims = TShiharaiM.objects.filter(user_id=user_id).filter(assert_cd=assert_cd).filter(shop_name=shop_name).filter(used_date=used_date)
        # shiharai_row = tshiharaims.count()
        initial_data = []
        # buyer_choice = []

        # mbuyers = MBuyer.objects.filter(user_id=user_id).order_by('buyerNm')
        # buyer_choice.append((' ', ''))
        # for buyer in mbuyers:
        #     buyer_choice.append((str(buyer.id), buyer.buyerNm))

        for shiharaim in tshiharaims:
            initial_data.append(
                {
                    'id' : shiharaim.id,
                    'item_nm' : shiharaim.item_nm,
                    'buyer_cd' : shiharaim.buyer_cd,
                    'sum_user_amt' : shiharaim.sum_user_amt,
                    'buyer_choice' : shiharaim.buyer_cd,
                    'shiharai_row' : shiharai_row,
                }
            )
            shiharai_row += 1

        if shiharai_row == 0:
            initial_data.append(
                {
                    'id' : None,
                    'item_nm' : '',
                    'buyer_cd' : ' ',
                    'sum_user_amt' : None,
                    'buyer_choice' : ' ',
                    'shiharai_row' : shiharai_row,
                }
            )
            shiharai_row += 1
        formset = TShiharaiMModelFormSet(request.GET or None, initial=initial_data)

        context = {
            'user_id': user_id,
            'user_name': user_name,
            'y': used_year,
            'm': used_month,
            'd': used_day,
            'shop_name': shop_name,
            'assert_cd': assert_cd,
            'formset': formset,
            'shiharai_total_row' : shiharai_row,
        }
        return render(request, 'tukuyomi/shiharaim_input.html',context)
    
    elif request.method == 'POST':
        formset = TShiharaiMModelFormSet(request.POST or None)
        now_datetime = timezone.datetime.now()
        shiharai_row = request.POST['shiharai_total_row']

        if formset.is_valid():
            # instances = formset.save(commit=False)
            # for form in instances:
            # return HttpResponse(len(formset))
            for form in formset:
                if form.is_valid():
                    id = form.cleaned_data['id']
                    delete_flg = form.cleaned_data['delete_flg']
                    tshiharaim = form.save(commit=False)
                    if delete_flg == True:
                        del_tshiharaim = TShiharaiM.objects.get(id=id)
                        del_tshiharaim.delete()
                    else:
                        if id is None or id=='':
                            # 新規
                            tshiharaim = TShiharaiM()
                            tshiharaim.user_id = user_id
                            tshiharaim.used_date = datetime(year=y,month=m,day=d)
                            tshiharaim.shop_name = shop_name
                            tshiharaim.assert_cd = assert_cd
                            tshiharaim.buyer_cd = form.cleaned_data['buyer_choice']
                            tshiharaim.item_nm = form.cleaned_data['item_nm']
                            tshiharaim.sum_user_amt = form.cleaned_data['sum_user_amt']
                            tshiharaim.create_pg_id   = 'assert_input'
                            tshiharaim.create_user_id = user_id
                            tshiharaim.create_date    = now_datetime
                            tshiharaim.update_pg_id   = 'assert_input'
                            tshiharaim.update_user_id = user_id
                            tshiharaim.update_date    = now_datetime
                        else:
                            # 更新
                            tshiharaim.id = id
                            tshiharaim.user_id = user_id
                            tshiharaim.used_date = datetime(year=y,month=m,day=d)
                            tshiharaim.shop_name = shop_name
                            tshiharaim.assert_cd = assert_cd
                            tshiharaim.buyer_cd = form.cleaned_data['buyer_choice']
                            tshiharaim.update_pg_id   = 'assert_input'
                            tshiharaim.update_user_id = user_id
                            tshiharaim.update_date    = now_datetime
                        tshiharaim.save()

            return redirect('/tukuyomi/shiharai_info/' + used_year + '/' + used_month + '/' + str(assert_cd))
        else:
            context = {
                'user_id': user_id,
                'user_name': user_name,
                'y': used_year,
                'm': used_month,
                'd': used_day,
                'shop_name': shop_name,
                'assert_cd': assert_cd,
                'formset': formset,
                'shiharai_row' : shiharai_row,
            }
            return render(request, 'tukuyomi/shiharaim_input.html',context)
