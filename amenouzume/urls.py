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
    url(r'^place_item/$', views.place_item, name='place_item'),
    url(r'^stock_data/$', views.stock_data, name='stock_data'),
    url(r'^stock_data_history/$', views.stock_data_history, name='stock_data_history'),
    # path('site_input/<int:id>', views.site_input, name='site_input'),
]
