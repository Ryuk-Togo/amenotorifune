from django.conf.urls import url
from django.urls import path
from . import views

app_name = "omoikane"
urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^main/$', views.main, name='main'),
    url(r'^login_input/$', views.login_input, name='login_input'),
    url(r'^user_list/$', views.user_list, name='user_list'),
    path('user_input_modify/<str:user_id>/<str:shori>/', views.user_input_modify, name='user_input_modify'),
    url(r'^user_input/$', views.user_input, name='user_input'),
    url(r'^menu_list/$', views.menu_list, name='menu_list'),
    path('menu_input_modify/<int:id>/<str:shori>/', views.menu_input_modify, name='menu_input_modify'),
    url(r'^menu_input/$', views.menu_input, name='menu_input'),

]
