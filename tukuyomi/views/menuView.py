from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
    reverse,
)
from django.http import HttpResponse
from django.utils import timezone
from django import forms
import datetime
from datetime import datetime
import logging
import os
from tukuyomi import tukuyomiConst
from tukuyomi.models.mbuyer import MBuyer

def menu(request):
    if request.method == 'GET':
        user_id = request.session.get('LOGIN_USER_ID')
        user_name = request.session.get('LOGIN_USER_NAME')

    # 定数初期化
    mbuyers = MBuyer.objects.filter(user_id=user_id).order_by('buyerNm')
    tukuyomiConst.BUYER_CHOICE.append((None, ''))
    for buyer in mbuyers:
        tukuyomiConst.BUYER_CHOICE.append((buyer.id, buyer.buyerNm))

    context = {
        'user_id':user_id,
        'user_name':user_name,
        'now_year':datetime.strftime(datetime.now(), '%Y'),
        'now_month':datetime.strftime(datetime.now(), '%m'),
        # 'now_year':datetime.strftime(datetime.today(), '%Y'),
        # 'now_month':datetime.strftime(datetime.today(), '%m'),
        'form': None,
    }

    return render(request, 'tukuyomi/menu.html',context)

