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
    SendRangeForm,
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
    # TKondateRecipe,
)
from sarutahiko import const
import calendar
import datetime
from datetime import datetime, date, timedelta
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
            try:
                mrecipe = MRecipe.objects.filter(user_id=user_id).get(recipe_name=recipe_name)
                form = RecipeForm(initial={
                    'id'          : mrecipe.id,
                    'recipe_name' : mrecipe.recipe_name,
                    'url'         :  mrecipe.url,
                })
            except:
                form = RecipeForm(initial={
                    'id'          : None,
                    'recipe_name' : recipe_name,
                    'url'         : '',
                })

            recipeItemData = []
            try:
                mrecipeItem = MRecipeItem.objects.filter(user_id=user_id).filter(recipe_id=mrecipe.id).order_by('row')
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
            except:
                pass
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

# def recipe_item(request,process,row):
#     user_id = request.session.get('LOGIN_USER_ID')
#     user_name = request.session.get('LOGIN_USER_NAME')
#     if request.method == 'GET':
#         form = RecipeForm(request.GET)
#         return HttpResponse(form)
#         RecipeItemFormSet = formsets.formset_factory(form=RecipeItemForm, extra=2,)
#         formSet = RecipeItemFormSet(request.GET or None)
#         return HttpResponse(formSet)
#         if process == 'i':
#             data = []
#             form_row = 0
#             return HttpResponse(formSet)
#             if formSet.is_valid():
#                 for recipe_item_form in formSet.cleaned_data:
#                     if str(form_row) == row:
#                         form_data = {
#                             'id':0,
#                             'row':str(form_row),
#                             'recipe_id':0,
#                             'item_id':'',
#                             'item_amt':0,
#                             'item_name':'',
#                         }
#                         data.append(form_data)
#                         form_row += 1

#                     form_data = {
#                         'id':recipe_item_form.cleaned_data['id'],
#                         'row':str(form_row),
#                         'recipe_id':recipe_item_form.cleaned_data['recipe_id'],
#                         'item_id':recipe_item_form.cleaned_data['item_id'],
#                         'item_amt':recipe_item_form.cleaned_data['item_amt'],
#                         'item_name':recipe_item_form.cleaned_data['item_name'],
#                     }
#                     data.append(form_data)
#                     form_row += 1
            
#             else:
#                 return HttpResponse(formSet.errors)

#             RecipeItemFormSet = formsets.formset_factory(form=RecipeItemForm, extra=form_row,)
#             formSet = RecipeItemFormSet(request.GET or None,initial=data)
#             context = {
#                 'user_id':user_id,
#                 'user_name':user_name,
#                 'now_year':datetime.strftime(datetime.now(), '%Y'),
#                 'now_month':datetime.strftime(datetime.now(), '%m'),
#                 'form':form,
#                 'formset':formSet,
#             }
#             return render(request, 'sarutahiko/recipe.html',context)

#     else:
#         return HttpResponse('POST')

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
    dt = date(year, month, 1)
    max_day = calendar.monthrange(dt.year, dt.month)[1]
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
    KondateFormSet  = formsets.formset_factory(form=KondateRecipeForm, extra=0)

    if request.method == 'GET':
        form = KondateForm(request.GET or None, initial={
            'year':year,
            'month':month,
            'day':day,
        })
        # 昼の主菜
        kondates  = TKondate.objects.filter(user_id=user_id).filter(recipe_date=date(year,month,day)).order_by('time','is_sub','id')
        kondateData = []
        blancHeck   = []
        for kondate in kondates:
            recipe_name = ""
            if kondate.recipe_id!='':
                try:
                    recipe = get_object_or_404(MRecipe,id=kondate.recipe_id)
                    recipe_name = recipe.recipe_name
                except:
                    recipe_name = ""
                
            kondateData.append({
                'id'               : kondate.id,
                'recipe_date'      : kondate.recipe_date,
                'time'             : kondate.time,
                'is_sub'           : kondate.is_sub,
                'recipe_id'        : kondate.recipe_id,
                'recipe_name'      : recipe_name,
                'number_of_people' : kondate.number_of_people,
            })

        if kondateData == blancHeck:
            kondateData.append({
                'id'               : '',
                'user_id'          : user_id,
                'recipe_date'      : date(year,month,day),
                'time'             : '0',
                'is_sub'           : '0',
                'recipe_id'        : '',
                'recipe_name'      : '',
                'number_of_people' : 0,
            })
            kondateData.append({
                'id'               : '',
                'user_id'          : user_id,
                'recipe_date'      : date(year,month,day),
                'time'             : '0',
                'is_sub'           : '1',
                'recipe_id'        : '',
                'recipe_name'      : '',
                'number_of_people' : 0,
            })
            kondateData.append({
                'id'               : '',
                'user_id'          : user_id,
                'recipe_date'      : date(year,month,day),
                'time'             : '1',
                'is_sub'           : '0',
                'recipe_id'        : '',
                'recipe_name'      : '',
                'number_of_people' : 0,
            })
            kondateData.append({
                'id'               : '',
                'user_id'          : user_id,
                'recipe_date'      : date(year,month,day),
                'time'             : '1',
                'is_sub'           : '1',
                'recipe_id'        : '',
                'recipe_name'      : '',
                'number_of_people' : 0,
            })

        kondateFormSet = KondateFormSet(request.GET or None, initial=kondateData)
        context = {
            'user_id'          :user_id,
            'user_name'        :user_name,
            'now_year'         :year,
            'now_month'        :month,
            'day'              :day,
            'form'             :form,
            'kondateFormSet'   :kondateFormSet,
        }
        return render(request, 'sarutahiko/kondate.html',context)
    
    else:
        kondateFormSet = KondateFormSet(request.POST)
        sysDate = datetime.now()

        if kondateFormSet.is_valid():
            for kondateForm in kondateFormSet:

                if kondateForm.cleaned_data['recipe_name'] is None or kondateForm.cleaned_data['recipe_name']=='':
                    if kondateForm.cleaned_data['id'] is not None:
                        # 元々データがあったが、レシピ名を消した
                        tkondates = TKondate.objects.filter(pk=kondateForm.cleaned_data['id'])
                        if tkondates.count()!=0:
                            for tkondate in tkondates:
                                tkondate.delete()
                    # 元々データが無かった場合は、何もしない
                else:
                    if kondateForm.cleaned_data['id'] is None:
                        # 元々データが無いが、新たに入力した
                        tkondate = TKondate()
                        tkondate.create_date    = sysDate
                        tkondate.create_pg_id   = 'sarutahiko.kondate'
                        tkondate.create_user_id = user_id
                    else:
                        # 元々データがあったので、更新した
                        tkondate = get_object_or_404(TKondate,pk=kondateForm.cleaned_data['id'])
                    tkondate.user_id          = user_id
                    tkondate.recipe_date      = date(year=year,month=month,day=day)
                    tkondate.time             = kondateForm.cleaned_data['time']
                    tkondate.is_sub           = kondateForm.cleaned_data['is_sub']
                    tkondate.number_of_people = kondateForm.cleaned_data['number_of_people']
                    tkondate.recipe_id        = kondateForm.cleaned_data['recipe_id']
                    tkondate.update_date      = sysDate
                    tkondate.update_pg_id     = 'sarutahiko.kondate'
                    tkondate.update_user_id   = user_id
                    tkondate.save()

            # データが無かった場合は、空データを挿入
            blank_kondate(request,'0','0',user_id,year,month,day,sysDate)
            blank_kondate(request,'0','1',user_id,year,month,day,sysDate)
            blank_kondate(request,'1','0',user_id,year,month,day,sysDate)
            blank_kondate(request,'1','1',user_id,year,month,day,sysDate)

            return redirect('/sarutahiko/menu_calendar/' + str(year) + '/' + str(month))

        else:
            return HttpResponse(kondateFormSet)

def blank_kondate(request,time,is_sub,user_id,year,month,day,sysDate):
    tkondates = TKondate.objects.filter(user_id=user_id).filter(recipe_date=date(year=year,month=month,day=day)).filter(time=time).filter(is_sub=is_sub)
    if tkondates.count()==0:
        tkondate = TKondate()
        tkondate.user_id          = user_id
        tkondate.recipe_date      = date(year=year,month=month,day=day)
        tkondate.time             = time
        tkondate.is_sub           = is_sub
        tkondate.number_of_people = 0
        tkondate.create_date      = sysDate
        tkondate.create_pg_id     = 'sarutahiko.kondate'
        tkondate.create_user_id   = user_id
        tkondate.update_date      = sysDate
        tkondate.update_pg_id     = 'sarutahiko.kondate'
        tkondate.update_user_id   = user_id
        tkondate.save()

    return
    
def item(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    sysDate = datetime.now()

    if request.method == 'GET':
        form = ItemModelForm(request.GET or None)

        context = {
            'user_id'  :user_id,
            'user_name':user_name,
            'now_year' :datetime.strftime(datetime.now(), '%Y'),
            'now_month':datetime.strftime(datetime.now(), '%m'),
            'form'     :form
        }
        return render(request, 'sarutahiko/item.html',context)

    else:
        form = ItemModelForm(request.POST)
        if form.is_valid():
            item_id = form.cleaned_data['id']
            if item_id is None:
                mitem = MItem()
                mitem.create_date    = sysDate
                mitem.create_pg_id   = 'sarutahiko.item'
                mitem.create_user_id = user_id
            else:
                mitem = get_object_or_404(MItem,id=item_id)
            
            mitem.user_id        = user_id
            mitem.item_name      = form.cleaned_data['item_name_upd']
            mitem.item_term      = 0
            mitem.update_date    = sysDate
            mitem.update_pg_id   = 'sarutahiko.item'
            mitem.update_user_id = user_id
            mitem.save()
            
        return redirect('/sarutahiko/menu/')

def send(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')

    if request.method == 'GET':

        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        form = SendRangeForm(request.GET or None, initial={
            'start_date':start_date,
            'end_date':None,
        })

        result = []
        itemName = {}
        if start_date is not None and end_date is not None:
            start_date_obj = datetime.strptime(start_date, '%Y/%m/%d')
            end_date_obj = datetime.strptime(end_date, '%Y/%m/%d')

            searchRange = (end_date_obj - start_date_obj).days + 1
            for day in range(searchRange):
                recipe_date = start_date_obj + timedelta(days=day)
                kondates = TKondate.objects.filter(user_id=user_id).filter(recipe_date=recipe_date).order_by('recipe_date','time','is_sub')
                lanch = []
                dinner = []

                for kondate in kondates:
                    if kondate.recipe_id is not None and kondate.recipe_id!='':
                        recipe = get_object_or_404(MRecipe,id=kondate.recipe_id)
                        if kondate.time=='0':
                            lanch.append({
                                'time'            :TIME[kondate.time],
                                'is_sub'          :IS_SUB[kondate.is_sub],
                                'recipe_name'     :recipe.recipe_name,
                                'number_of_people':kondate.number_of_people,
                            })
                        else:
                            dinner.append({
                                'time'            :TIME[kondate.time],
                                'is_sub'          :IS_SUB[kondate.is_sub],
                                'recipe_name'     :recipe.recipe_name,
                                'number_of_people':kondate.number_of_people,
                            })

                        # レシピの材料を追加する
                        recipeItems = MRecipeItem.objects.filter(user_id=user_id).filter(recipe_id=kondate.recipe_id)
                        for recipeItem in recipeItems:
                            item = get_object_or_404(MItem,pk=recipeItem.item_id)
                            try:
                                itemName[item.item_name] = itemName[item.item_name] + (recipeItem.item_amt * kondate.number_of_people)
                            except:
                                itemName[item.item_name] = recipeItem.item_amt * kondate.number_of_people


                result.append({
                    'recipe_date':recipe_date.strftime('%Y/%m/%d'),
                    'lanch'   :lanch,
                    'dinner'  :dinner,
                })
        
        context = {
            'user_id'  :user_id,
            'user_name':user_name,
            'now_year' :datetime.strftime(datetime.now(), '%Y'),
            'now_month':datetime.strftime(datetime.now(), '%m'),
            'form'     :form,
            'result'   :result,
            'itemName':itemName,
        }
        return render(request, 'sarutahiko/send.html',context)

    else:
        form = SendRangeForm(request.POST)
            
        return redirect('/sarutahiko/menu/')

TIME = dict([
    ['0','昼食'],
    ['1','夕食'],
])

IS_SUB = dict([
    ['0','主菜'],
    ['1','副菜'],
])

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
            except:
                recipeItemAmt = 0
            
            result.append({
                'item_name':item.item_name,
                'item_id'  :item.id,
                'item_amt' :recipeItemAmt,
            })
        return JsonResponse(result,safe=False)
