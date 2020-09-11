from django.conf.urls import url
from django.urls import path
from . import views

app_name = "amenouzume"
urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^place/$', views.place, name='place'),
    url(r'^place_input/$', views.place_input, name='place_input'),
    path('place_input_modify/<int:id>/<str:shori>', views.place_input_modify, name='place_input_modify'),
    url(r'^item/$', views.item, name='item'),
    url(r'^item_input/$', views.item_input, name='item_input'),
    path('item_input_modify/<int:id>/<str:shori>', views.item_input_modify, name='item_input_modify'),
    url(r'^place_item/$', views.place_item, name='place_item'),
    url(r'^place_item_list/$', views.place_item_list, name='place_item_list'),
    url(r'^stock_data/$', views.stock_data, name='stock_data'),
    url(r'^stock_data_history/$', views.stock_data_history, name='stock_data_history'),
    url(r'^get_users/$', views.get_users, name='get_users'),
    # url(r'^download_stock_data/$', views.download_stock_data, name='download_stock_data'),
    path('download_stock_data/<str:user_id>', views.download_stock_data, name='download_stock_data'),
    path('download_user_data', views.download_user_data, name='download_user_data'),
    path('download_place_data/<str:user_id>', views.download_place_data, name='download_place_data'),
    path('download_item_data/<str:user_id>', views.download_item_data, name='download_item_data'),
    # path('upload_stock_data/<str:stocks>', views.upload_stock_data, name='upload_stock_data'),
    url(r'^upload_stock_data/$', views.upload_stock_data, name='upload_stock_data'),
    url(r'^upload_stock_data_test/$', views.upload_stock_data_test, name='upload_stock_data_test'),
]
