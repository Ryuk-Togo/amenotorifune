from django.conf.urls import url
from . import views
from susanowo.views.inboxviews import *

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^index/$', views.index, name='index'),
    url(r'^inbox/$', inbox, name='inbox'),
    url(r'^inbox/submit/$', inbox, name='inbox_submit'),
]
