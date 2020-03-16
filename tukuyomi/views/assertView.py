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
from tukuyomi.models.massert import MAssert
from tukuyomi.forms.assertForm import AssertModelForm

def assert_list(request):
    # AssertListModelFormSet = forms.modelformset_factory(
    #     MAssert,
    #     fields = ('id','assertNm'),
    # )
    
    if request.method == 'GET':
        user_id = request.session.get('LOGIN_USER_ID')
        user_name = request.session.get('LOGIN_USER_NAME')

        # formSet = AssertListModelFormSet(queryset=MAssert.objects.filter(user_id=user_id).order_by('assertNm'))
        massert = MAssert.objects.filter(user_id=user_id).order_by('assert_nm')

        context = {
            'user_id':user_id,
            'user_name':user_name,
            'form': massert,
        }

        return render(request, 'tukuyomi/assert_list.html',context)

def assert_input(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')

    if request.method == 'GET':
        form = AssertModelForm(request.GET or None)

        context = {
            'user_id':user_id,
            'user_name':user_name,
            'form': form,
            'shori': '',
        }
        return render(request, 'tukuyomi/assert_input.html',context)
    
    elif request.method == 'POST':
        form = AssertModelForm(request.POST or None)
        if form.is_valid():
            massert = form.save(commit=False)
            massert.user_id = user_id
            massert.create_pg_id   = 'assert_input'
            massert.create_user_id = user_id
            massert.update_pg_id   = 'assert_input'
            massert.update_user_id = user_id
            massert.save()
            return redirect('/tukuyomi/assert_list/')
        else:
            context = {
                'user_id':user_id,
                'user_name':user_name,
                'form': form,
                'shori': '',
            }
            return render(request, 'tukuyomi/assert_input.html',context)

def assert_input_modify(request,id,shori):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')

    if request.method == 'GET':
        massert = MAssert.objects.get(id=id)
        form = AssertModelForm(request.GET or None,instance=massert)

        context = {
            'user_id':user_id,
            'user_name':user_name,
            'form': form,
            'shori': shori,
            'id': id,
        }
        return render(request, 'tukuyomi/assert_input.html',context)
    
    elif request.method == 'POST':
        form = AssertModelForm(request.POST)
        if form.is_valid():
            massert = form.save(commit=False)
            massert = get_object_or_404(MAssert, id=id)
            if shori=='m':
                massert.assert_nm       = request.POST['assertNm']
                massert.update_date    = timezone.datetime.now()
                massert.update_pg_id   = 'assert_input'
                massert.update_user_id = user_id
                massert.save()
            elif shori=='d':
                massert.delete()
            return redirect('/tukuyomi/assert_list/')
        else:
            context = {
                'user_id':user_id,
                'user_name':user_name,
                'form': form,
                'shori':shori,
                'id': id,
            }
            return render(request, 'tukuyomi/assert_input.html',context)
