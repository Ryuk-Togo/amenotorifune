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
from tukuyomi.models.massert import MAssert
from tukuyomi.models.mbuyer import MBuyer
from tukuyomi.models.tshiharaim import TShiharaiM
# from tukuyomi.forms.henkinForm import HenkinHeaderForm, HenkingakuForm, HenkinListForm
from tukuyomi.forms.henkinForm import HenkinHeaderForm, HenkinListForm
from django.forms import formsets

HenkinListFormSet = formsets.formset_factory(form=HenkinListForm, extra=0,)

def henkin_header(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')

    if request.method == 'GET':
        form_header = HenkinHeaderForm(request.GET or None)
        # form_henkingaku = HenkingakuForm(request.GET or None)
        buyer_id = request.GET.get('buyer_name', None)
        formSet = HenkinListFormSet()

        form_header = get_user_name_list(form_header, user_id)
        if buyer_id is None or buyer_id=='':
            form_header.fields['buyer_name'].initial = [' ']
        else:
            form_header.fields['buyer_name'].initial = [user_id]
        # form_header.fields['row_count'].initial = 0
        
        context = {
            'user': form_header,
            'user_id': user_id,
            'user_name': user_name,
            # 'henkingaku': form_henkingaku,
            'formset': formSet,
            'now_year':datetime.strftime(datetime.now(), '%Y'),
            'now_month':datetime.strftime(datetime.now(), '%m'),
        }
        return render(request, 'tukuyomi/henkin.html',context)

    elif request.method == 'POST':
        buyer_id = request.POST['buyer_name']
        form_header = HenkinHeaderForm(request.POST or None)
        form_header = get_user_name_list(form_header, user_id)
        form_header.fields['buyer_name'].initial = [buyer_id]
        # form_henkingaku = HenkingakuForm(request.POST or Nonfrom tukuyomi.forms.henkinForm import HenkinHeaderForm, HenkingakuForm, HenkinListForm
        formSet = HenkinListFormSet(request.POST or None)
        row_count = 0

        henkin_list = []
        sql = ''
        sql = sql + 'SELECT s.id , s.user_id , s.used_date , s.shop_name , a.assert_nm , s.item_nm , s.sum_user_amt , refund_balance , s.assert_cd , s.buyer_cd  '
        sql = sql + '  FROM "tukuyomi_tshiharaim" as s '
        sql = sql + ' INNER JOIN "tukuyomi_massert" as a '
        sql = sql + '         ON (s.assert_cd=a.id) '
        sql = sql + ' WHERE s.user_id = %(user_id)s '
        sql = sql + '   AND s.buyer_cd = %(buyer_id)s '
        sql = sql + '   AND s.sum_user_amt > s.refund_balance '
        sql = sql + ' ORDER BY s.used_date , s.shop_name , a.assert_nm , s.item_nm '

        data = None
        if buyer_id == ' ':
            sql_buyer_id = None
        else:
            sql_buyer_id = buyer_id

        henkin_list = []
        with connection.cursor() as cursor:
            cursor.execute(sql, 
                {
                    'user_id': user_id, 
                    'buyer_id': sql_buyer_id, 
                }
            )
            sqldata = cursor.fetchall()

            for rec in sqldata:
                data = {
                    'id': rec[0],
                    'user_id': rec[1],
                    'used_date': rec[2],
                    'shop_name': rec[3],
                    'assert_nm': rec[4],
                    'item_nm': rec[5],
                    'sum_user_amt': rec[6],
                    'refund_balance': rec[7],
                    'assert_cd': rec[8],
                    'buyer_cd': rec[9],
                    'moto_refund_balance': rec[7],
                }
                henkin_list.append(data)
                row_count+=1
        formSet = HenkinListFormSet(initial=henkin_list)
        form_header.fields['row_count'].initial = row_count

        context = {
            'user':form_header,
            'user_id': user_id,
            'user_name': user_name,
            'cmb_buyer_id':buyer_id,
            # 'henkingaku': form_henkingaku,
            'formset':formSet,
            'now_year':datetime.strftime(datetime.now(), '%Y'),
            'now_month':datetime.strftime(datetime.now(), '%m'),
        }
        return render(request, 'tukuyomi/henkin.html',context)

# def henkin_input(request):
#     user_id = request.session.get('LOGIN_USER_ID')
#     user_name = request.session.get('LOGIN_USER_NAME')
#     if request.method == 'POST':
#         form_header = HenkinHeaderForm(request.POST or None)
#         formSet = HenkinListFormSet(request.POST or None)
#         # form_henkingaku = HenkingakuForm(request.POST or None)
#         # buyer_id = form_header.fields['buyer_name']
#         # row_count = form_henkingaku.fields['row_count']

#         context = {
#             'user': form_header,
#             'user_id': user_id,
#             'user_name': user_name,
#             # 'cmb_buyer_id': buyer_id,
#             # 'henkingaku': form_henkingaku,
#             'formset': formSet,
#             # 'row_count': row_count,
#         }
#         return render(request, 'tukuyomi/henkin.html',context)

def henkin_list(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'POST':
        form_header = HenkinHeaderForm(request.POST or None)
        formSet = HenkinListFormSet(request.POST or None)
        buyer_id = request.POST['buyer_id']
        # buyer_id = form_header.cleaned_data['buyer_name']
        now_datetime = timezone.datetime.now()
        # row_count = request.POST['row_count']

        if formSet.is_valid():
            for form in formSet:
                if form.is_valid():
                    is_selected = form.cleaned_data['is_selected']
                    tshiharaim = form.save(commit=False)
                    if is_selected:
                        refund_balance = form.cleaned_data['refund_balance']
                        tshiharaim.id             = form.cleaned_data['id']
                        # tshiharaim.user_id        = user_id
                        # tshiharaim.assert_cd      = form.cleaned_data['assert_cd']
                        # tshiharaim.buyer_cd       = form.cleaned_data['buyer_cd']
                        tshiharaim.refund_balance = refund_balance
                        tshiharaim.update_pg_id   = 'assert_input'
                        tshiharaim.update_user_id = user_id
                        tshiharaim.update_date    = now_datetime
                        tshiharaim.save()

        # context = {
        #     'user': form_header,
        #     'user_id': user_id,
        #     'user_name': user_name,
        #     'cmb_buyer_id': buyer_id,
        #     # 'henkingaku': form_henkingaku,
        #     'formset': formSet,
        #     # 'row_count': row_count,
        # }
        # return render(request, 'tukuyomi/henkin.html',context)
        return redirect('/tukuyomi/menu/')

def get_user_name_list(form_header, user_id):
    musers = MBuyer.objects.filter(user_id=user_id).order_by('id')
    user_choice = []
    user_choice.append((' ', ''))
    for user in musers:
        user_choice.append((user.id, user.buyerNm))

    form_header.fields['buyer_name'].choices = user_choice
    return form_header
