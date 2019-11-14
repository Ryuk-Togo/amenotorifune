from django.conf.urls import url
from . import views

app_name = "susanowo"
urlpatterns = [
    url(r'^$', views.indexviews.login, name='login'),
    url(r'^index/$', views.indexviews.index, name='index'),
    url(r'^inbox/$', views.inboxviews.inbox, name='inbox'),
    url(r'^inboxupd/$', views.inboxviews.inboxupd, name='inboxupd'),
    url(r'^modstatus/$', views.indexviews.modstatus, name='modstatus'),
]
