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
    RecipeItemFormSet = formsets.formset_factory(form=RecipeItemForm, extra=0)
    if request.method == 'GET':
        # data = []
        # form_data = {
        #     'id':0,
        #     'row':'0',
        #     'recipe_id':0,
        #     'item_id':0,
        #     'item_amt':0,
        #     'item_name':'',
        # }
        # form_data = dict(id=0,row='0',recipe_id=0,item_id=0,item_amt=0,item_name='')
        # data.append(form_data)

        form = RecipeForm(request.GET or None)
        # formSet = RecipeItemFormSet()
        # formSet = RecipeItemFormSet(initial=data)
        # RecipeItemFormSet = formsets.formset_factory(form=RecipeItemForm, extra=0)
        # formSet = RecipeItemFormSet()
        formSet = RecipeItemFormSet(request.GET or None)
        
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
        form = RecipeForm(request.POST)
        formSet = RecipeItemFormSet(request.POST)
        sysDate = datetime.now()

        # レシピマスタ登録
        if form.is_valid():
            # recipe_data = form.save(commit=False)
            recipe_id = request.POST['recipe_id']

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

            # return HttpResponse(form)
        else:
            return HttpResponse(form.errors)

        # レシピ材料登録
        if formSet.is_valid():
            # recipeItems = formSet.save(commit=False)

            # レシピ材料を洗い替え削除
            recipeItems = MRecipeItem.objects.filter(recipe_id=request.POST['recipe_id'])
            recipeItems.delete()
            rowCnt = 0

            for recipe_item_form in formSet:

                # レシピ材料を登録
                if recipe_item_form.cleaned_data['item_name'] != "":
                    recipeItem = MRecipeItem()
                    recipeItem.user_id        = user_id
                    recipeItem.recipe_id      = request.POST['recipe_id']
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
                # recipeItem = recipe_item_form.save(commit=False)
                # return HttpResponse(recipe_item_form.cleaned_data['item_name'])
                # recipeItem = MRecipeItem.objects.get(pk=recipe_item.id)
                # recipeItem = MRecipeItem()
                # recipeItem.user_id = user_id
                # recipeItem.recipe_id = recipe_item.recipe_id
                # recipeItem.item_id = recipe_item.item_id
                # recipeItem.item_amt = recipe_item.item_amt
                # recipeItem.row = rowCnt
                # recipeItem.create_date    = sysDate
                # recipeItem.create_pg_id   = 'sarutahiko.recipe'
                # recipeItem.create_user_id = user_id
                # recipeItem.update_date    = sysDate
                # recipeItem.update_pg_id   = 'sarutahiko.recipe'
                # recipeItem.update_user_id = user_id

            # return HttpResponse(formSet)

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
            return HttpResponse(formSet.errors)


    return render(request, 'sarutahiko/recipe.html',context)

# def recipe(request,recipe_name):
#     user_id = request.session.get('LOGIN_USER_ID')
#     user_name = request.session.get('LOGIN_USER_NAME')
#     RecipeItemFormSet = formsets.formset_factory(form=RecipeItemForm, extra=0)
#     if request.method == 'GET':
#         form = RecipeForm(request.GET or None)
#         formSet = RecipeItemFormSet(request.GET or None)
#         context = {
#             'user_id':user_id,
#             'user_name':user_name,
#             'now_year':datetime.strftime(datetime.now(), '%Y'),
#             'now_month':datetime.strftime(datetime.now(), '%m'),
#             'form':form,
#             'formset':formSet,
#         }
#         return render(request, 'sarutahiko/recipe.html',context)
#     else:
#         form = RecipeForm(request.POST)
#         formSet = RecipeItemFormSet(request.POST)
#         sysDate = datetime.now()

#         # レシピマスタ登録
#         if form.is_valid():
#             recipe_id = request.POST['recipe_id']

#             if recipe_id is None or recipe_id == "":
#                 recipe = MRecipe()
#                 recipe.create_date    = sysDate
#                 recipe.create_pg_id   = 'sarutahiko.recipe'
#                 recipe.create_user_id = user_id
#             else:
#                 recipe = get_object_or_404(MRecipe,id=int(recipe_id))

#             recipe.user_id     = user_id
#             recipe.recipe_name = form.cleaned_data['recipe_name']
#             recipe.url         = form.cleaned_data['url']
#             recipe.update_date    = sysDate
#             recipe.update_pg_id   = 'sarutahiko.recipe'
#             recipe.update_user_id = user_id
#             recipe.save()

#         else:
#             return HttpResponse(form.errors)

#         # レシピ材料登録
#         if formSet.is_valid():
#             # レシピ材料を洗い替え削除
#             recipeItems = MRecipeItem.objects.filter(recipe_id=request.POST['recipe_id'])
#             recipeItems.delete()
#             rowCnt = 0

#             for recipe_item_form in formSet:
#                 # レシピ材料を登録
#                 if recipe_item_form.cleaned_data['item_name'] != "":
#                     recipeItem = MRecipeItem()
#                     recipeItem.user_id        = user_id
#                     recipeItem.recipe_id      = request.POST['recipe_id']
#                     recipeItem.item_id        = recipe_item_form.cleaned_data['item_id']
#                     recipeItem.item_amt       = recipe_item_form.cleaned_data['item_amt']
#                     recipeItem.row            = rowCnt
#                     recipeItem.create_date    = sysDate
#                     recipeItem.create_pg_id   = 'sarutahiko.recipe'
#                     recipeItem.create_user_id = user_id
#                     recipeItem.update_date    = sysDate
#                     recipeItem.update_pg_id   = 'sarutahiko.recipe'
#                     recipeItem.update_user_id = user_id
#                     recipeItem.save()
#                     rowCnt += 1

#             context = {
#                 'user_id':user_id,
#                 'user_name':user_name,
#                 'now_year':datetime.strftime(datetime.now(), '%Y'),
#                 'now_month':datetime.strftime(datetime.now(), '%m'),
#                 'form':form,
#                 'formset':formSet,
#             }
            
#             return render(request, 'sarutahiko/recipe.html',context)

#         else:
#             return HttpResponse(formSet.errors)


#     return render(request, 'sarutahiko/recipe.html',context)

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

def recipe_list(request,recipe_name):
    user_id = request.session.get('LOGIN_USER_ID')
    # user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        recipes = MRecipe.objects.filter(user_id=user_id).filter(recipe_name__icontains=recipe_name).order_by('recipe_name')
        result = []
        for recipe in recipes:
            recipeItems = MRecipeItem.objects.filter(user_id=user_id).filter(recipe_id=recipe.id).order_by('row')
            itemResult = []
            # for recipeItem in recipeItems:
            #     item = MItem.objects.filter(user_id=user_id).filter(id=recipeItem.item_id)
            #     itemResult.append({
            #         'recipe_id':recipe.id,
            #         'id'       :recipeItem.id,
            #         'item_name':item.item_name,
            #         'item_id'  :recipeItem.item_id,
            #         'item_amt' :recipeItem.item_amt,
            #         'row'      :recipeItem.row,
            #     })

            result.append({
                'code' :recipe.id,
                'name' :recipe.recipe_name,
                'url'  :recipe.url,
                # 'items':itemResult,
            })
            # result.append(recipe.recipe_name)
        return JsonResponse(result,safe=False)

def item_list(request,recipe_id,item_name):
    user_id = request.session.get('LOGIN_USER_ID')
    # user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
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
            
            # if recipeItem is not None:
            #     recipe_item_amt = recipeItem.item_amt
            result.append({
                # 'code': item.id,
                # 'name': item.item_name,
                # 'amt' : recipe_item_amt,
                'recipe_id':recipe_id,
                'id'       :recipeItemId,
                'item_name':item.item_name,
                'item_id'  :item.id,
                'item_amt' :recipeItemAmt,
                'row'      :recipeItemRow,
            })
            # result.append(recipe.recipe_name)
        return JsonResponse(result,safe=False)
