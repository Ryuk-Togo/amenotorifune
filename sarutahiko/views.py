from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
)
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db.models import Q

from sarutahiko.forms import (
    LoginModelForm,
    RecipeForm,
    RecipeItemForm,
    KondateForm,
    KondateRecipeForm,
    ItemModelForm,
    # RecipeItemFormSet,
    KondateItemFormSet,
)
from omoikane.models import (
    MUser,
)
from amenouzume.models import (
    MItem,
)
from sarutahiko.models import (
    MRecipe,
    MRecipeItem,
    TKondate,
    TKondateRecipe,
)
from datetime import datetime, date, timedelta
import calendar
import logging
import os
from izanagi import settings
from django.forms import formsets
import json
from django.http.response import JsonResponse

# Create your views here.
# ログイン画面
def login(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        if not (user_id is None and user_name is None):
            # year = timezone.strftime('%Y')
            # month = timezone.strftime('%m')
            # return redirect('/sarutahiko/calendar%year=' + year + '&month=' + month)
            return redirect('/sarutahiko/menu/')

        form = LoginModelForm(request.GET or None)
        context = {
            'user_id':user_id,
            'user_name':user_name,
            'form': form
        }
        return render(request, 'sarutahiko/login.html',context)
    elif request.method == 'POST':
        form = LoginModelForm(request.POST)
        if not form.is_valid():
            context = {
                'form': form
            }
            return render(request, 'sarutahiko/login.html', context)
        
        user_id = request.POST['user_id']
        user = MUser.objects.get(user_id=user_id)
        user_name = user.user_name
        request.session['LOGIN_USER_ID'] = user.user_id
        request.session['LOGIN_USER_NAME'] = user.user_name

        context = {
            'user_id':user_id,
            'user_name':user_name,
        }

        return redirect('/sarutahiko/menu/')
        # return render(request, 'amenouzume/menu.html',context)

def menu(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        today = datetime.today()
        yyyy = datetime.strftime(today, '%Y')
        mm = datetime.strftime(today, '%m')
        # context = {
        #     'user_id':user_id,
        #     'user_name':user_name,
        # }
    return redirect('/sarutahiko/menu_calendar/' + yyyy + '/' + mm)

def recipe(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        data = []
        form_data = {
            'id':0,
            'row':'0',
            'recipe_id':0,
            'item_id':0,
            'item_amt':0,
            'item_name':'',
        }
        # form_data = dict(id=0,row='0',recipe_id=0,item_id=0,item_amt=0,item_name='')
        data.append(form_data)

        form = RecipeForm(request.GET or None)
        # formSet = RecipeItemFormSet()
        # formSet = RecipeItemFormSet(initial=data)
        RecipeItemFormSet = formsets.formset_factory(form=RecipeItemForm, extra=0,)
        # formSet = RecipeItemFormSet()
        formSet = RecipeItemFormSet(request.GET or None,initial=data)
        
        context = {
            'user_id':user_id,
            'user_name':user_name,
            'now_year':datetime.strftime(datetime.now(), '%Y'),
            'now_month':datetime.strftime(datetime.now(), '%m'),
            'form':form,
            'formset':formSet,
        }
        return render(request, 'sarutahiko/recipe.html',context)
    # else:

    return render(request, 'sarutahiko/recipe.html',context)

def recipe_item(request,process,row):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        form = RecipeForm(request.GET)
        return HttpResponse(form)
        # recipeItemFormSet = RecipeItemFormSet(request.GET or None)
        # formSet = recipeItemFormSet.save(commit=False)
        RecipeItemFormSet = formsets.formset_factory(form=RecipeItemForm, extra=2,)
        formSet = RecipeItemFormSet(request.GET or None)
        return HttpResponse(formSet)
        if process == 'i':
            data = []
            form_row = 0
            # return HttpResponse(formSet.is_valid())
            return HttpResponse(formSet)
            if formSet.is_valid():
                for recipe_item_form in formSet.cleaned_data:
                    if str(form_row) == row:
                        form_data = {
                            'id':0,
                            'row':str(form_row),
                            'recipe_id':0,
                            'item_id':'',
                            'item_amt':0,
                            'item_name':'',
                        }
                        data.append(form_data)
                        form_row += 1

                    form_data = {
                        'id':recipe_item_form.cleaned_data['id'],
                        'row':str(form_row),
                        'recipe_id':recipe_item_form.cleaned_data['recipe_id'],
                        'item_id':recipe_item_form.cleaned_data['item_id'],
                        'item_amt':recipe_item_form.cleaned_data['item_amt'],
                        'item_name':recipe_item_form.cleaned_data['item_name'],
                    }
                    data.append(form_data)
                    form_row += 1
            
            else:
                return HttpResponse(formSet.errors)


            # for recipe_item_form in formSet:
            #     if formSet.is_valid():
            #         if str(form_row) == row:
            #             form_data = {
            #                 'id':None,
            #                 'row':str(form_row),
            #                 'recipe_id':0,
            #                 'item_id':'',
            #                 'item_amt':0,
            #                 'item_name':'',
            #             }
            #             data.append(form_data)
            #             form_row += 1

            #         form_data = {
            #             'id':recipe_item_form.cleaned_data['id'],
            #             'row':str(form_row),
            #             'recipe_id':recipe_item_form.cleaned_data['recipe_id'],
            #             'item_id':recipe_item_form.cleaned_data['item_id'],
            #             'item_amt':recipe_item_form.cleaned_data['item_amt'],
            #             'item_name':recipe_item_form.cleaned_data['item_name'],
            #         }
            #         data.append(form_data)
            #         form_row += 1

            #     else:
            #         return HttpResponse(formSet.errors)


            # formSet = RecipeItemFormSet(initial=data)
            RecipeItemFormSet = formsets.formset_factory(form=RecipeItemForm, extra=form_row,)
            formSet = RecipeItemFormSet(request.GET or None,initial=data)
            context = {
                'user_id':user_id,
                'user_name':user_name,
                'now_year':datetime.strftime(datetime.now(), '%Y'),
                'now_month':datetime.strftime(datetime.now(), '%m'),
                'form':form,
                'formset':formSet,
            }
            return render(request, 'sarutahiko/recipe.html',context)

    else:
        return HttpResponse('POST')



def menu_calendar(request, year, month):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        week_date = [0,0,0,0,0,0,0]
        month_day = []
        month_range = calendar.monthrange(year, month)

        for day in list(range(1, month_range[1]+1)):
            date = (day + month_range[0]) % 7

            week_date[date] = day
            if date == 6:
                month_day.append(week_date)

                if day != month_range[1]:
                    week_date = [0,0,0,0,0,0,0]


            # if day == month_range[1]:
        month_day.append(week_date)
    
        context = {
            'user_id':user_id,
            'user_name':user_name,
            'now_year':year,
            'now_month':month,
            'month_data':month_day,
            # 'now_year':datetime.strftime(datetime.now(), '%Y'),
            # 'now_month':datetime.strftime(datetime.now(), '%m'),
        }

        return render(request, 'sarutahiko/menu_calendar.html',context)

def kondate(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    context = {
        'user_id':user_id,
        'user_name':user_name,
        'now_year':datetime.strftime(datetime.now(), '%Y'),
        'now_month':datetime.strftime(datetime.now(), '%m'),
    }
    return render(request, 'sarutahiko/kondate.html',context)

def item(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    context = {
        'user_id':user_id,
        'user_name':user_name,
        'now_year':datetime.strftime(datetime.now(), '%Y'),
        'now_month':datetime.strftime(datetime.now(), '%m'),
    }
    return render(request, 'sarutahiko/item.html',context)

def send(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    context = {
        'user_id':user_id,
        'user_name':user_name,
        'now_year':datetime.strftime(datetime.now(), '%Y'),
        'now_month':datetime.strftime(datetime.now(), '%m'),
    }
    return render(request, 'sarutahiko/send.html',context)
