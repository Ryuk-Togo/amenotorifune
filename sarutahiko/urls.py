from django.conf.urls import url
from django.urls import path
from . import views

app_name = "sarutahiko"
urlpatterns = [
    url(r'^$', views.login, name='login'),
    # url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^menu/$', views.menu, name='menu'),
    path('menu_calendar/<int:year>/<int:month>', views.menu_calendar, name='menu_calendar'),
    url(r'^recipe/$', views.recipe, name='recipe'),
    path('recipe_item/<str:process>/<str:row>', views.recipe_item, name='recipe_item'),
    url(r'^kondate/$', views.kondate, name='kondate'),
    url(r'^item/$', views.item, name='item'),
    url(r'^send/$', views.send, name='send'),
]
