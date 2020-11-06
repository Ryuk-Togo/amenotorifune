from django.conf.urls import url
from django.urls import path
from . import views

app_name = "sarutahiko"
urlpatterns = [
    url(r'^$', views.login, name='login'),
    # url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^menu/$', views.menu, name='menu'),
    path('menu_calendar/<int:year>/<int:month>', views.menu_calendar, name='menu_calendar'),
    path('recipe/<str:recipe_name>', views.recipe, name='recipe'),
    # url(r'^kondate/$', views.kondate, name='kondate'),
    path('kondate/<int:year>/<int:month>/<int:day>', views.kondate, name='kondate'),
    url(r'^item/$', views.item, name='item'),
    url(r'^send/$', views.send, name='send'),
    path('recipe_list/<str:recipe_name>/<str:proccess>', views.recipe_list, name='recipe_list'),
    path('item_list/<int:recipe_id>/<str:item_name>/<str:proccess>', views.item_list, name='item_list'),
]
