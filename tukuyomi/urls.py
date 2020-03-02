from django.conf.urls import url
from django.urls import path
from . import views

app_name = "tukuyomi"
urlpatterns = [
    url(r'^$', views.loginView.login, name='login'),
    url(r'^menu/$', views.menuView.menu, name='menu'),
    url(r'^assert_list/$', views.assertView.assert_list, name='assert_list'),
    url(r'^assert_input/$', views.assertView.assert_input, name='assert_input'),
    path('assert_input_modify/<int:id>/<str:shori>', views.assertView.assert_input_modify, name='assert_input_modify'),
    url(r'^buyer_list/$', views.buyerView.buyer_list, name='buyer_list'),
    url(r'^buyer_input/$', views.buyerView.buyer_input, name='buyer_input'),
    path('buyer_input_modify/<int:id>/<str:shori>', views.buyerView.buyer_input_modify, name='buyer_input_modify'),
]
