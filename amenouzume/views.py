from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
)
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from django import forms
from amenouzume.forms import (
    LoginModelForm,
    PlaceModelForm,
    PlaceDeleteModelForm,
    ItemModelForm,
    ItemDeleteModelForm,
    ItemListFormSet,
    PlaceHeaderForm,
    ItemListForm,
    ItemListFormSet,
    StockItemFormSet,
    # StockItemForm,
    StockDataFormSet,
    StockDataFormTest,
)
from amenouzume.models import (
    MPlace,
    MItem,
    MItemPlace,
    TStock,
    TStockHistory,
)
from omoikane.models import (
    MUser,
)
import datetime
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
            return redirect('/amenouzume/menu/')

        form = LoginModelForm(request.GET or None)
        context = {
            'user_id':user_id,
            'user_name':user_name,
            'form': form
        }
        return render(request, 'amenouzume/login.html',context)
    elif request.method == 'POST':
        form = LoginModelForm(request.POST)
        if not form.is_valid():
            context = {
                'form': form
            }
            return render(request, 'amenouzume/login.html', context)
        
        user_id = request.POST['user_id']
        user = MUser.objects.get(user_id=user_id)
        user_name = user.user_name
        request.session['LOGIN_USER_ID'] = user.user_id
        request.session['LOGIN_USER_NAME'] = user.user_name

        context = {
            'user_id':user_id,
            'user_name':user_name,
        }

        return redirect('/amenouzume/menu/')
        # return render(request, 'amenouzume/menu.html',context)

def menu(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        context = {
            'user_id':user_id,
            'user_name':user_name,
        }

    return render(request, 'amenouzume/menu.html',context)

def place(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        mplaces = MPlace.objects.filter(user_id=user_id).order_by('place_name')
        context = {
            'user_id':user_id,
            'user_name':user_name,
            'forms':mplaces
        }
    elif request.method == 'POST':
        return redirect('/amenouzume/place_input/')
        
    return render(request, 'amenouzume/place.html',context)

def place_input(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        form = PlaceModelForm()
        context = {
            'user_id':user_id,
            'user_name':user_name,
            'form': form,
            'shori': '',
        }
        return render(request, 'amenouzume/place_input.html',context)
    elif request.method == 'POST':
        form = PlaceModelForm(request.POST)
        if not form.is_valid():
            context = {
                'user_id':user_id,
                'user_name':user_name,
                'form': form,
                'shori': '',
            }
            return render(request, 'amenouzume/place_input.html', context)
        mplace = form.save(commit=False)
        mplace.user_id        = user_id
        mplace.place_name     = form.cleaned_data['place_name']
        mplace.create_pg_id   = 'amenouzume.place_input'
        mplace.create_user_id = user_id
        mplace.update_pg_id   = 'amenouzume.place_input'
        mplace.update_user_id = user_id
        mplace.save()

        return redirect('/amenouzume/place/')
    
def place_input_modify(request, id, shori):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        mplace = MPlace.objects.get(id=id)
        form = PlaceModelForm(instance=mplace)
        context = {
            'user_id': user_id,
            'user_name':user_name,
            'form': form,
            'id': id,
            'shori': shori,
        }
        return render(request, 'amenouzume/place_input.html',context)
    elif request.method == 'POST':
        mplace = get_object_or_404(MPlace, id=id)
        if shori=='m':
            form = PlaceModelForm(request.POST)
            if not form.is_valid():
                context = {
                    'user_id': user_id,
                    'user_name':user_name,
                    'form': form,
                    'id': id,
                    'shori': shori,
                }
                return render(request, 'amenouzume/place_input.html',context)
            
            mplace.place_name = form.cleaned_data['place_name']
            mplace.update_date = timezone.datetime.now()
            mplace.update_pg_id = 'amenouzume.place_input'
            mplace.updaet_user_id = user_id
            mplace.save()
            return redirect('/amenouzume/place/')

        elif shori=='d':
            form = PlaceDeleteModelForm(request.POST)
            if not form.is_valid():
                context = {
                    'form': form,
                    'user_id': user_id,
                    'user_name':user_name,
                    'id': id,
                    'shori': shori,
                }
                return render(request, 'amenouzume/place_input.html',context)
            
            mplace.delete()
            return redirect('/amenouzume/place/')
    
def item(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        mitems = MItem.objects.filter(user_id=user_id).order_by('item_name')
        context = {
            'user_id':user_id,
            'user_name':user_name,
            'forms':mitems
        }
    elif request.method == 'POST':
        return redirect('/amenouzume/item_input/')
        
    return render(request, 'amenouzume/item.html',context)

def item_input(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        form = ItemModelForm()
        context = {
            'user_id':user_id,
            'user_name':user_name,
            'form': form,
            'shori': '',
        }
        return render(request, 'amenouzume/item_input.html',context)
    elif request.method == 'POST':
        form = ItemModelForm(request.POST)
        if not form.is_valid():
            context = {
                'user_id':user_id,
                'user_name':user_name,
                'form': form,
                'shori': '',
            }
            return render(request, 'amenouzume/item_input.html', context)
        mitem = form.save(commit=False)
        mitem.user_id        = user_id
        mitem.item_name      = form.cleaned_data['item_name']
        mitem.safety_amt     = form.cleaned_data['safety_amt']
        mitem.item_term      = form.cleaned_data['item_term']
        mitem.create_pg_id   = 'amenouzume.item_input'
        mitem.create_user_id = user_id
        mitem.update_pg_id   = 'amenouzume.item_input'
        mitem.update_user_id = user_id
        mitem.save()

        return redirect('/amenouzume/item/')
    
def item_input_modify(request, id, shori):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        mitem = MItem.objects.get(id=id)
        if shori=='m':
            form = ItemModelForm(instance=mitem)
        else:
            form = ItemDeleteModelForm(instance=mitem)
        
        context = {
            'user_id': user_id,
            'user_name':user_name,
            'form': form,
            'id': id,
            'shori': shori,
        }
        return render(request, 'amenouzume/item_input.html',context)
    elif request.method == 'POST':
        mitem = get_object_or_404(MItem, id=id)
        if shori=='m':
            form = ItemModelForm(request.POST)
            if not form.is_valid():
                context = {
                    'user_id': user_id,
                    'user_name':user_name,
                    'form': form,
                    'id': id,
                    'shori': shori,
                }
                return render(request, 'amenouzume/item_input.html',context)
            
            mitem.item_name      = form.cleaned_data['item_name']
            mitem.safety_amt     = form.cleaned_data['safety_amt']
            mitem.item_term      = form.cleaned_data['item_term']
            mitem.update_date    = timezone.datetime.now()
            mitem.update_pg_id   = 'amenouzume.item_input'
            mitem.updaet_user_id = user_id
            mitem.save()
            return redirect('/amenouzume/item/')

        elif shori=='d':
            form = ItemDeleteModelForm(request.POST)
            if not form.is_valid():
                context = {
                    'form': form,
                    'user_id': user_id,
                    'user_name':user_name,
                    'id': id,
                    'shori': shori,
                }
                return render(request, 'amenouzume/item_input.html',context)
            
            mitem.delete()
            return redirect('/amenouzume/item/')

def place_item(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        form_header = PlaceHeaderForm(request.GET or None)
        place_id = request.GET.get('place_name', None)
        formSet = ItemListFormSet()

        # form_header = get_place_list(form_header)
        # if user_id is None or user_id=='':
        #     form_header.fields['place_name'].initial = [' ']

        # else:
        #     form_header.fields['place_name'].initial = [user_id]

        form_header = get_place_list(form_header,user_id)
        form_header.fields['place_name'].initial = [' ']

        context = {
            'place':form_header,
            'user_id': user_id,
            'user_name':user_name,
            'formSet':formSet,
        }

        return render(request, 'amenouzume/place_item.html',context)

    elif request.method == 'POST':
        form_header = PlaceHeaderForm(request.POST or None)
        form_header = get_place_list(form_header,user_id)
        place_id = request.POST['place_name']
        form_header.fields['place_name'].initial = [place_id]

        mitems = MItem.objects.filter(user_id=user_id).order_by('item_name')
        item_list = []

        for item in mitems:
            is_select = False

            try:
                itemPlace = get_object_or_404(MItemPlace, user_id=user_id, place_id=place_id, item_id=item.id)
            except:
                itemPlace = None

            if itemPlace is not None:
                is_select = True

            item_list.append({
                'is_select': is_select,
                'item_id': item.id,
                'item_name': item.item_name,
            })

        formSet = ItemListFormSet(initial=item_list)
        context = {
            'place':form_header,
            'user_id': user_id,
            'user_name':user_name,
            'cmb_place_id':place_id,
            'formSet':formSet,
        }

        return render(request, 'amenouzume/place_item.html',context)

def place_item_list(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'POST':
        place_id = request.POST['place_id']
        form_header = PlaceHeaderForm(request.POST or None)
        formSets = ItemListFormSet(request.POST or None)

        mitemplace = MItemPlace.objects.filter(user_id=user_id, place_id=place_id)
        mitemplace.delete()

        if formSets.is_valid():
            for formSet in formSets:
                if formSet.cleaned_data['is_select']:
                    item_id = formSet.cleaned_data['item_id']
                    itemPlace = MItemPlace()
                    itemPlace.user_id       = user_id
                    itemPlace.place_id      = place_id
                    itemPlace.item_id       = item_id
                    itemPlace.dwonload_date = None
                    itemPlace.upload_date   = None
                    itemPlace.save()

        else:
            context = {
                'place':form_header,
                'user_id': user_id,
                'user_name':user_name,
                'cmb_place_id':place_id,
                'formSet':formSets,
            }

        return render(request, 'amenouzume/place_item.html',context)

def stock_data(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        stock_data = []
        mplace = MPlace.objects.filter(user_id=user_id).order_by('place_name')
        for place in mplace:
            mitemplaces = MItemPlace.objects.filter(user_id=user_id, place_id=place.id).order_by('item_id')
            tstock = TStock.objects.filter(place_id=place.id)
            is_inserted = False
            if tstock:
                is_inserted = True
            item_data = []
            for itemplace in mitemplaces:
                mitem = MItem.objects.get(id=itemplace.item_id)
                item_data.append({
                    'id':itemplace.id,
                    'item_id':mitem.id,
                    'item_name':mitem.item_name,
                    'safety_amt':mitem.safety_amt,
                })
            
            place = {
                'place_id':place.id,
                'place_name':place.place_name,
                'item':item_data,
                'is_inserted':is_inserted
            }
            stock_data.append(place)

        context = {
            'user_id':user_id,
            'user_name':user_name,
            'stock_data':stock_data,
        }

        return render(request, 'amenouzume/stock_data.html',context)
    else:
        selected_list = request.POST.getlist('is_selected')
        now_timestamp = timezone.datetime.now()
        for id in selected_list:
            mitemplace = MItemPlace.objects.filter(place_id=id)
            for data in mitemplace:
                mitem = MItem.objects.get(id=data.item_id)
                tstock = TStock()
                tstock.user_id        = user_id
                tstock.place_id       = data.place_id
                tstock.item_id        = data.item_id
                tstock.item_name      = mitem.item_name
                tstock.item_amt       = 0
                tstock.safety_amt     = mitem.safety_amt
                tstock.buy_amt        = 0
                tstock.download_date  = now_timestamp
                tstock.create_pg_id   = 'amenouzume.stock_data'
                tstock.create_user_id = user_id
                tstock.update_pg_id   = 'amenouzume.stock_data'
                tstock.update_user_id = user_id
                tstock.save()

        context = {
            'user_id':user_id,
            'user_name':user_name,
            # 'stock_data':stock_data,
        }

        return render(request, 'amenouzume/menu.html',context)


def stock_data_history(request):
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')
    if request.method == 'GET':
        context = {
            'user_id':user_id,
            'user_name':user_name,
        }

    return render(request, 'amenouzume/menu.html',context)

def get_place_list(form_header,user_id):
    mplaces = MPlace.objects.filter(user_id=user_id).order_by('place_name')
    place_choice = []
    place_choice.append((' ', ''))
    for place in mplaces:
        place_choice.append((place.id, place.place_name))

    form_header.fields['place_name'].choices = place_choice
    return form_header

def get_users(request):
    ret = []
    musers = MUser.objects.all().order_by('user_id')
    for user in musers:
        data = {
            'user_id':user.user_id
        }
        ret.append(data)
    # return HttpResponse(musers)
    return JsonResponse(ret,safe=False)


def download_stock_data(request,user_id):
    if request.method == 'GET':
        ret = []
        tstocks = TStock.objects.filter(user_id=user_id).order_by('place_id')
        now_timestamp = timezone.datetime.now()
        for stock in tstocks:
            place_data = MPlace.objects.get(id=stock.place_id)
            data = {
                'id'         :stock.id,
                'user_id'    :stock.user_id,
                'place_id'   :stock.place_id,
                'place_name' :place_data.place_name,
                'item_id'    :stock.item_id,
                'item_name'  :stock.item_name,
                'item_amt'   :stock.item_amt,
                'safety_amt' :stock.safety_amt,
                'buy_amt'    :stock.buy_amt,
            }
            ret.append(data)
            stock.download_date  = now_timestamp
            stock.update_date    = now_timestamp
            stock.update_user_id = user_id
            stock.update_pg_id   = 'amenouzume.download_stock_data'
            stock.save()
        # jstocks = json.loads(tstocks)
        return JsonResponse(ret,safe=False)

def download_place_data(request,user_id):
    if request.method == 'GET':
        ret = []
        mplaces = MPlace.objects.filter(user_id=user_id).order_by('id')
        for place in mplaces:
            data = {
                'id'         :place.id,
                'place_name' :place.place_name,
            }
            ret.append(data)
        # jstocks = json.loads(tstocks)
        return JsonResponse(ret,safe=False)

def download_item_data(request,user_id):
    if request.method == 'GET':
        ret = []
        mitems = MItem.objects.filter(user_id=user_id).order_by('id')
        for item in mitems:
            data = {
                'id'        :item.id,
                'item_name' :item.item_name,
            }
            ret.append(data)
        # jstocks = json.loads(tstocks)
        return JsonResponse(ret,safe=False)

@csrf_exempt
def upload_stock_data(request):

    if request.method == 'POST':
        json_stocks = None
        now_timestamp = timezone.datetime.now()
        ret = []

        try:
            # json_stocks = json.loads(request.json)
            json_stocks = json.loads(request.body.decode('utf-8'))
        except Exception as e:
            context = {
                'message' : e,
                'return'  : False,
            }
            ret.append(context)
            return JsonResponse(ret,safe=False)

        for stock_data in json_stocks:
            try:
                tstock = TStock.objects.get(id=stock_data["id"])
            except:
                tstock = TStock()

            tstock.user_id        = stock_data["user_id"]
            tstock.item_name      = stock_data["item_name"]
            tstock.place_id       = stock_data["place_id"]
            tstock.item_id        = stock_data["item_id"]
            tstock.item_amt       = stock_data["item_amt"]
            tstock.safety_amt     = stock_data["safety_amt"]
            tstock.buy_amt        = stock_data["buy_amt"]
            tstock.download_date  = datetime.datetime.strptime(stock_data["download_date"],'%Y/%m/%d %H:%M:%S')
            tstock.upload_date    = now_timestamp
            tstock.update_date    = now_timestamp
            tstock.update_user_id = stock_data["user_id"]
            tstock.update_pg_id   = 'StockChecker'
            tstock.save()

        context = {
            'message' :"正常に受信しました。",
            'return'  : True,
        }
        ret.append(context)
        return JsonResponse(ret,safe=False)

    else:
        user_id = request.session.get('LOGIN_USER_ID')
        user_name = request.session.get('LOGIN_USER_NAME')
        tstocks = TStock.objects.all()
        # form = StockDataFormTest(tstocks)
        # print(tstocks)
        # formSet = StockItemFormTestSet(initial=tstocks)

        ret = []
        for stock in tstocks:
            data = {
                'id'         :stock.id,
                # 'user_id'    :stock.user_id,
                'place_id'   :stock.place_id,
                'item_id'    :stock.item_id,
                'item_name'  :stock.item_name,
                # 'item_amt'   :stock.item_amt,
                'safety_amt' :stock.safety_amt,
                # 'buy_amt'    :stock.buy_amt,
            }
            form = StockDataFormTest(data)
            ret.append(form)
        context = {
            'user_id'  : user_id,
            'user_name': user_name,
            'form'     : ret,
            # 'form'     : form,
            # 'form'     : formSet,
        }
        return render(request, 'amenouzume/stock_data_test.html',context)

    return HttpResponse('<p>Not Fund 404.</p>')


def download_user_data(request):
    if request.method == 'GET':
        ret = []
        musers = MUser.objects.all().order_by('user_id')
        for user in musers:
            data = {
                'user_id'    :user.user_id,
                'user_name'  :user.user_name,
            }
            ret.append(data)
        # jstocks = json.loads(tstocks)
        return JsonResponse(ret,safe=False)

def upload_stock_data_test(request):
    
    user_id = request.session.get('LOGIN_USER_ID')
    user_name = request.session.get('LOGIN_USER_NAME')

    if request.method == 'POST':
        stock_data_list = request.POST.getlist('user_id')
        message = request.POST.get('message',"null")

        ret = []
        for stock_id in stock_data_list:
            # stock = TStock.objects.get(user_id=stock_id)
            # data = {
            #     'id'         :stock.id,
            #     'user_id'    :stock.user_id,
            #     'place_id'   :stock.place_id,
            #     'item_id'    :stock.item_id,
            #     'item_name'  :stock.item_name,
            #     'item_amt'   :stock.item_amt,
            #     'safety_amt' :stock.safety_amt,
            #     'buy_amt'    :stock.buy_amt,
            # }
            data = {
                'user_id':stock_id
            }
            form = StockDataFormTest(data)
            ret.append(form)

        context = {
            'user_id'  : user_id,
            'user_name': user_name,
            'form'     : ret,
            # 'message'  : "post success.",
            'message'  : "post success. " + message,
        }

        return render(request, 'amenouzume/stock_data_test.html',context)

    else:
        tstocks = TStock.objects.all()

        ret = []
        for stock in tstocks:
            data = {
                'id'         :stock.id,
                'user_id'    :stock.user_id,
                'place_id'   :stock.place_id,
                'item_id'    :stock.item_id,
                'item_name'  :stock.item_name,
                'item_amt'   :stock.item_amt,
                'safety_amt' :stock.safety_amt,
                'buy_amt'    :stock.buy_amt,
            }
            form = StockDataFormTest(data)
            ret.append(form)
            # ret.append(data)
        context = {
            'user_id'  : user_id,
            'user_name': user_name,
            'form'     : ret,
            'message'  : "get success.",
        }
        return render(request, 'amenouzume/stock_data_test.html',context)
