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
import calendar
import datetime
from datetime import datetime, date, timedelta
# from dateutil.relativedelta import relativedelta
# import dateutil
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

def menu(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        today = datetime.today()
        yyyy = datetime.strftime(today, '%Y')
        mm = datetime.strftime(today, '%m')
    return redirect('/sarutahiko/menu_calendar/' + yyyy + '/' + mm)

def recipe(request,recipe_name):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    RecipeItemFormSet = formsets.formset_factory(form=RecipeItemForm, extra=0)

    if request.method == 'GET':
        if recipe_name.strip() == '':
            form = RecipeForm(initial={
                'id'          : 0,
                'recipe_name' : '',
                'url'         : '',
            })
            formSet = RecipeItemFormSet(request.GET or None)
        else:
            mrecipe = MRecipe.objects.filter(user_id=user_id).get(recipe_name=recipe_name)
            form = RecipeForm(initial={
                'id'          : mrecipe.id,
                'recipe_name' : mrecipe.recipe_name,
                'url'         :  mrecipe.url,
            })
            mrecipeItem = MRecipeItem.objects.filter(user_id=user_id).filter(recipe_id=mrecipe.id).order_by('row')
            recipeItemData = []
            for recipeItem in mrecipeItem:
                mitem = MItem.objects.get(id=recipeItem.item_id)
                recipeItemData.append({
                    'id'       :recipeItem.id,
                    'recipe_id':mrecipe.id,
                    'item_id'  :recipeItem.item_id,
                    'item_name':mitem.item_name,
                    'item_amt' :recipeItem.item_amt,
                    'row'      :recipeItem.row,
                })
            formSet = RecipeItemFormSet(initial=recipeItemData)

        context = {
            'user_id':user_id,
            'user_name':user_name,
            'now_year':datetime.strftime(datetime.now(), '%Y'),
            'now_month':datetime.strftime(datetime.now(), '%m'),
            'form':form,
            'formset':formSet,
            'recipe_name':recipe_name,
        }
        return render(request, 'sarutahiko/recipe.html',context)
    else:
        form = RecipeForm(request.POST)
        formSet = RecipeItemFormSet(request.POST)
        sysDate = datetime.now()

        # レシピマスタ登録
        if form.is_valid():
            recipe_id = request.POST['id']

            if recipe_id is None or recipe_id == "":
                recipe = MRecipe()
                recipe.create_date    = sysDate
                recipe.create_pg_id   = 'sarutahiko.recipe'
                recipe.create_user_id = user_id
            else:
                recipe = get_object_or_404(MRecipe,id=int(recipe_id))

            recipe.user_id     = user_id
            recipe.recipe_name = form.cleaned_data['recipe_name']
            recipe.url         = form.cleaned_data['url']
            recipe.update_date    = sysDate
            recipe.update_pg_id   = 'sarutahiko.recipe'
            recipe.update_user_id = user_id
            recipe.save()

        else:
            return HttpResponse(form.errors)

        # レシピ材料登録
        if formSet.is_valid():
            # レシピ材料を洗い替え削除
            recipeItems = MRecipeItem.objects.filter(recipe_id=request.POST['id'])
            recipeItems.delete()
            rowCnt = 0

            for recipe_item_form in formSet:
                # レシピ材料を登録
                if recipe_item_form.cleaned_data['item_name'] != "":
                    recipeItem = MRecipeItem()
                    recipeItem.user_id        = user_id
                    recipeItem.recipe_id      = request.POST['id']
                    recipeItem.item_id        = recipe_item_form.cleaned_data['item_id']
                    recipeItem.item_amt       = recipe_item_form.cleaned_data['item_amt']
                    recipeItem.row            = rowCnt
                    recipeItem.create_date    = sysDate
                    recipeItem.create_pg_id   = 'sarutahiko.recipe'
                    recipeItem.create_user_id = user_id
                    recipeItem.update_date    = sysDate
                    recipeItem.update_pg_id   = 'sarutahiko.recipe'
                    recipeItem.update_user_id = user_id
                    recipeItem.save()
                    rowCnt += 1

            context = {
                'user_id':user_id,
                'user_name':user_name,
                'now_year':datetime.strftime(datetime.now(), '%Y'),
                'now_month':datetime.strftime(datetime.now(), '%m'),
                'form':form,
                'formset':formSet,
                'recipe_name':recipe_name,
            }
            
            return redirect('/sarutahiko/recipe/%20')
        else:
            return HttpResponse(formSet.errors)

def recipe_item(request,process,row):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        form = RecipeForm(request.GET)
        return HttpResponse(form)
        RecipeItemFormSet = formsets.formset_factory(form=RecipeItemForm, extra=2,)
        formSet = RecipeItemFormSet(request.GET or None)
        return HttpResponse(formSet)
        if process == 'i':
            data = []
            form_row = 0
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

        if week_date[6] != month_range[1]:
            month_day.append(week_date)
        changeMonth = linkMonth(year,month)
    
        context = {
            'user_id'   :user_id,
            'user_name' :user_name,
            'now_year'  :year,
            'now_month' :month,
            'month_data':month_day,
            'prevYear'  :changeMonth['prevYear'],
            'prevMonth' :changeMonth['prevMonth'],
            'nextYear'  :changeMonth['nextYear'],
            'nextMonth' :changeMonth['nextMonth'],
        }

        return render(request, 'sarutahiko/menu_calendar.html',context)

def linkMonth(year,month):
    # dt = datetime.date(year, month, 1)
    # dt = datetime(year, month, 1)
    dt = date(year, month, 1)
    max_day = calendar.monthrange(dt.year, dt.month)[1]
    # prevMonth = datetime.date(dt.year, dt.month, dt.date) - datetime.timedelta(days=1)
    # nextMonth = datetime.date(dt.year, dt.month, max_day) + datetime.timedelta(days=1)
    prevMonth = date(dt.year, dt.month, dt.day) - timedelta(days=1)
    nextMonth = date(dt.year, dt.month, max_day) + timedelta(days=1)
    result = {
        'prevYear' :datetime.strftime(prevMonth, '%Y'),
        'prevMonth':datetime.strftime(prevMonth, '%m'),
        'nextYear' :datetime.strftime(nextMonth, '%Y'),
        'nextMonth':datetime.strftime(nextMonth, '%m'),
    }
    return result

def kondate(request,year,month,day):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    LanchMainKondateFormSet  = formsets.formset_factory(form=KondateRecipeForm, extra=1)
    LanchSubKondateFormSet   = formsets.formset_factory(form=KondateRecipeForm, extra=1)
    DinnerMainKondateFormSet = formsets.formset_factory(form=KondateRecipeForm, extra=1)
    DinnerSubKondateFormSet  = formsets.formset_factory(form=KondateRecipeForm, extra=1)
    if request.method == 'GET':
        form = KondateForm(request.GET or None, initial={
            'year':year,
            'month':month,
            'day':day,
        })
        # 昼の主菜
        lanchMains  = TKondate.objects.filter(user_id=user_id).filter(recipe_date=date(year,month,day)).filter(time='1').filter(is_main=True).order_by('id')
        lanchMainData = []
        for lanchMain in lanchMains:
            lanchMainData.append({
                'id'               : lanchMain.id,
                'user_id'          : lanchMain.user_id,
                'recipe_date'      : lanchMain.recipe_date,
                'time'             : lanchMain.time,
                'is_main'          : lanchMain.is_main,
                'recipe_id'        : lanchMain.recipe_id,
                'number_of_people' : lanchMain.number_of_people,
            })
        lanchMainFormSet = LanchMainKondateFormSet(request.GET or None, initial=lanchMainData)

        # 昼の副菜
        lanchSubs   = TKondate.objects.filter(user_id=user_id).filter(recipe_date=date(year,month,day)).filter(time='1').filter(is_main=False).order_by('id')
        lanchSubData = []
        for lanchSub in lanchSubs:
            lanchSubData.append({
                'id'               : lanchSub.id,
                'user_id'          : lanchSub.user_id,
                'recipe_date'      : lanchSub.recipe_date,
                'time'             : lanchSub.time,
                'is_main'          : lanchSub.is_main,
                'recipe_id'        : lanchSub.recipe_id,
                'number_of_people' : lanchSub.number_of_people,
            })
        lanchSubFormSet = LanchSubKondateFormSet(request.GET or None, initial=lanchSubData)

        # 夜の主菜
        dinnerMains = TKondate.objects.filter(user_id=user_id).filter(recipe_date=date(year,month,day)).filter(time='2').filter(is_main=True).order_by('id')
        dinnerMainData = []
        for dinnerMain in dinnerMains:
            dinnerMainData.append({
                'id'               : dinnerMain.id,
                'user_id'          : dinnerMain.user_id,
                'recipe_date'      : dinnerMain.recipe_date,
                'time'             : dinnerMain.time,
                'is_main'          : dinnerMain.is_main,
                'recipe_id'        : dinnerMain.recipe_id,
                'number_of_people' : dinnerMain.number_of_people,
            })
        dinnerMainFormSet = DinnerMainKondateFormSet(request.GET or None, initial=dinnerMainData)
        # 夜の副菜
        dinnerSubs  = TKondate.objects.filter(user_id=user_id).filter(recipe_date=date(year,month,day)).filter(time='2').filter(is_main=False).order_by('id')
        dinnerSubData = []
        for dinnerSub in dinnerSubs:
            dinnerSubData.append({
                'id'               : dinnerSub.id,
                'user_id'          : dinnerSub.user_id,
                'recipe_date'      : dinnerSub.recipe_date,
                'time'             : dinnerSub.time,
                'is_main'          : dinnerSub.is_main,
                'recipe_id'        : dinnerSub.recipe_id,
                'number_of_people' : dinnerSub.number_of_people,
            })
        dinnerSubFormSet = DinnerSubKondateFormSet(request.GET or None, initial=dinnerSubData)
    
    else:
        form = KondateForm(request.POST)
        # lanchMainFormSet  = LanchMainKondateFormSet(request.POST)
        # lanchSubFormSet   = LanchSubKondateFormSet(request.POST)
        # dinnerMainFormSet = DinnerMainKondateFormSet(request.POST)
        # dinnerSubFormSet  = DinnerSubKondateFormSet(request.POST)

        post_lanchMainFormSet  = request.POST.copy()
        lanchSubFormSet   = request.POST.copy()
        dinnerMainFormSet = request.POST.copy()
        dinnerSubFormSet  = request.POST.copy()

        lanchMainFormSet = LanchMainKondateFormSet(post_lanchMainFormSet )

        return HttpResponse(lanchMainFormSet)

    context = {
        'user_id'          :user_id,
        'user_name'        :user_name,
        'now_year'         :year,
        'now_month'        :month,
        'day'              :day,
        'form'             :form,
        'lanchMainFormSet' :lanchMainFormSet,
        'lanchSubFormSet'  :lanchSubFormSet,
        'dinnerMainFormSet':dinnerMainFormSet,
        'dinnerSubFormSet' :dinnerSubFormSet,
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

def recipe_list(request,recipe_name,proccess):
    user_id = request.session.get('LOGIN_USER_ID')
    # user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        if proccess=='C':
            recipes = MRecipe.objects.filter(user_id=user_id).filter(recipe_name=recipe_name).order_by('recipe_name')
        else:
            recipes = MRecipe.objects.filter(user_id=user_id).filter(recipe_name__icontains=recipe_name).order_by('recipe_name')
        result = []
        for recipe in recipes:
            itemResult = []

            result.append({
                'code' :recipe.id,
                'name' :recipe.recipe_name,
                'url'  :recipe.url,
            })
        return JsonResponse(result,safe=False)

def item_list(request,recipe_id,item_name,proccess):
    user_id = request.session.get('LOGIN_USER_ID')
    # user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        if proccess=='C':
            items = MItem.objects.filter(user_id=user_id).filter(item_name=item_name).order_by('item_name')
        else:
            items = MItem.objects.filter(user_id=user_id).filter(item_name__icontains=item_name).order_by('item_name')
        result = []
        for item in items:
            recipeItem = MRecipeItem.objects.filter(user_id=user_id).filter(recipe_id=recipe_id).filter(item_id=item.id)
            try:
                recipeItemAmt = recipeItem.item_amt
                recipeItemId  = recipeItem.id
                recipeItemRow = recipeItem.row
            except:
                recipeItemAmt = 0
                recipeItemId  = ""
                recipeItemRow = ""
            
            result.append({
                'item_name':item.item_name,
                'item_id'  :item.id,
                'item_amt' :recipeItemAmt,
            })
        return JsonResponse(result,safe=False)
