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

def riyou_info_init(request):
    if request.method == 'GET':
        year = datetime.strftime(datetime.today(), '%Y')
        month = datetime.strftime(datetime.today(), '%m')
        return redirect('/tukuyomi/riyou_info/' + year + '/' + month + '/')

def riyou_info(request,y,m):
    if request.method == 'GET':
        user_id = request.session.get('LOGIN_USER_ID')
        user_name = request.session.get('LOGIN_USER_NAME')

        used_year = ''
        used_month = ''
        try:
            used_year = datetime.strftime(datetime(year=y,month=m,day=1), '%Y')
            used_month = datetime.strftime(datetime(year=y,month=m,day=1), '%m')
        except:
            raise forms.ValidationError("日付が異常です。")

        next_y = datetime.strftime(add_month(datetime(year=y,month=m,day=1), 1), '%Y')
        next_m = datetime.strftime(add_month(datetime(year=y,month=m,day=1), 1), '%m')
        prev_y = datetime.strftime(add_month(datetime(year=y,month=m,day=1),-1), '%Y')
        prev_m = datetime.strftime(add_month(datetime(year=y,month=m,day=1),-1), '%m')
        next_prev = {
            'next_y': next_y,
            'next_m': next_m,
            'prev_y': prev_y,
            'prev_m': prev_m,
        }
        
        sql = ''
        sql = sql + 'SELECT at.assert_nm, at.id, COALESCE(sum(sh.used_amt),0) '
        sql = sql + '  FROM tukuyomi_massert at '
        sql = sql + '  LEFT OUTER JOIN tukuyomi_tshiharaih sh '
        sql = sql + '  ON ( sh.assert_cd = at.id '
        sql = sql + '   AND sh.user_id = at.user_id ) '
        sql = sql + ' WHERE at.user_id = %(user_id)s '
        sql = sql + '   AND ( sh.used_date is null '
        sql = sql + '    OR to_char(sh.used_date, \'yyyy/mm\') = %(used_month)s) '
        sql = sql + ' GROUP BY at.assert_nm, at.id '
        sql = sql + ' ORDER BY at.assert_nm '
        
        data = None
        form = []
        with connection.cursor() as cursor:
            cursor.execute(sql, 
                {
                    'user_id': user_id, 
                    'used_month': used_year + '/' + used_month,
                }
            )
            sqldata = cursor.fetchall()

            for rec in sqldata:
                data = {
                    'assert_nm': rec[0],
                    'assert_id': rec[1],
                    'sum_amt': rec[2],
                }
                form.append(data)

        context = {
            'user_id':user_id,
            'user_name':user_name,
            'used_year':used_year,
            'used_month':used_month,
            'form': form,
            'next_prev': next_prev,
        }

        return render(request, 'tukuyomi/riyou_info.html',context)

def add_month(base_date, months):
    """月の増減を行う"""
    month = base_date.month - 1 + months
    year = int(base_date.year + month / 12 )
    month = month % 12 + 1
    # day = min(base_date.day,calendar.monthrange(year,month)[1])
    return datetime(year=year,month=month,day=1)
