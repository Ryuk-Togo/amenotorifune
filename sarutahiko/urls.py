from django.conf.urls import url
from django.urls import path
from . import views

app_name = "sarutahiko"
urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^recipe/$', views.recipe, name='recipe'),
    url(r'^kondate/$', views.kondate, name='kondate'),
    url(r'^item/$', views.item, name='item'),
    url(r'^send/$', views.send, name='send'),
]
