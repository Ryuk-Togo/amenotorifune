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
from tukuyomi.forms.assertForm import AssertModelForm
import calendar

def shiharai_info(request,y,m,assert_cd):
    if request.method == 'GET':
        user_id = request.session.get('LOGIN_USER_ID')
        user_name = request.session.get('LOGIN_USER_NAME')

        massert = MAssert.objects.get(id=assert_cd)

        used_year = ''
        used_month = ''
        try:
            used_year = datetime.strftime(datetime(year=y,month=m,day=1), '%Y')
            used_month = datetime.strftime(datetime(year=y,month=m,day=1), '%m')
        except:
            raise forms.ValidationError("日付が異常です。")

        sql = ''
        sql = sql + 'SELECT to_char(sh.used_date,\'yyyy/mm/dd\'), sh.shop_name, sh.used_amt, sh.receipt, sh.id '
        sql = sql + '  FROM tukuyomi_tshiharaih sh '
        sql = sql + ' WHERE sh.user_id = %(user_id)s '
        sql = sql + '   AND to_char(sh.used_date, \'yyyy/mm\') = %(used_ym)s '
        sql = sql + '   AND sh.assert_cd = %(assert_cd)s '
        sql = sql + ' ORDER BY sh.used_date '
        
        data = None
        form = []
        with connection.cursor() as cursor:
            cursor.execute(sql, 
                {
                    'user_id': user_id, 
                    'used_ym': datetime.strftime(datetime(year=y,month=m,day=1), '%Y/%m'),
                    'assert_cd': assert_cd, 
                }
            )
            sqldata = cursor.fetchall()

            for rec in sqldata:
                data = {
                    'used_date': rec[0],
                    'shop_name': rec[1],
                    'used_amt': rec[2],
                    'receipt': rec[3],
                    'id': rec[4],
                }
                form.append(data)

        context = {
            'user_id':user_id,
            'user_name':user_name,
            'assert_cd': assert_cd,
            'assert_nm': massert.assert_nm,
            'used_year': used_year,
            'used_month': used_month,
            'form': form,
            'now_year':datetime.strftime(datetime.now(), '%Y'),
            'now_month':datetime.strftime(datetime.now(), '%m'),
        }

        return render(request, 'tukuyomi/shiharai_info.html',context)
