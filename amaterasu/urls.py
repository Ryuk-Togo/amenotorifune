from django.conf.urls import url
from django.urls import path
from . import views

app_name = "amaterasu"
urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^menu/$', views.menu, name='menu'),
    path('site_input/<int:id>', views.site_input, name='site_input'),
]
