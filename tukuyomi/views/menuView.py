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

def menu(request):
    if request.method == 'GET':
        user_id = request.session.get('LOGIN_USER_ID')
        user_name = request.session.get('LOGIN_USER_NAME')
        context = {
            'user_id':user_id,
            'user_name':user_name,
            'form': None,
        }

        return render(request, 'tukuyomi/menu.html',context)
