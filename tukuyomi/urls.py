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
    url(r'^riyou_info/$', views.riyouView.riyou_info_init, name='riyou_info_init'),
    path('riyou_info/<int:y>/<int:m>', views.riyouView.riyou_info, name='riyou_info'),
    path('shiharai_info/<int:y>/<int:m>/<int:assert_cd>', views.shiharaiView.shiharai_info, name='shiharai_info'),
    # url(r'^shiharaih_input/$', views.shiharaihView.shiharaih_input, name='shiharaih_input'),
    path('shiharaih_input/<int:assert_cd>', views.shiharaihView.shiharaih_input, name='shiharaih_input'),
    path('shiharaih_input_modify/<int:shiharaih_id>/<str:shori>', views.shiharaihView.shiharaih_input_modify, name='shiharaih_input_modify'),
    path('shiharaim_input/<int:assert_cd>/<int:y>/<int:m>/<int:d>/<str:shop_name>', views.shiharaimView.shiharaim_input, name='shiharaim_input'),
    # path('shiharaim_insert/<int:assert_cd>/<int:y>/<int:m>/<int:d>/<str:shop_name>/<int:insert_row>', views.shiharaimView.shiharaim_insert, name='shiharaim_insert'),
    # path('shiharaim_delete/<int:assert_cd>/<int:y>/<int:m>/<int:d>/<str:shop_name>/<int:delete_row>', views.shiharaimView.shiharaim_delete, name='shiharaim_delete'),
    url(r'^henkin_header/$', views.henkinView.henkin_header, name='henkin_header'),
    url(r'^henkin_list/$', views.henkinView.henkin_list, name='henkin_list'),
    # url(r'^henkin_input/$', views.henkinView.henkin_input, name='henkin_input'),
]
