from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.indexviews.login, name='login'),
    url(r'^index/$', views.indexviews.index, name='index'),
    url(r'^inbox/$', views.inboxviews.inbox, name='inbox'),
    url(r'^inbox/submit/$', views.inboxviews.inbox_submit, name='inbox_submit'),
]
