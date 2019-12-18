from django.conf.urls import url
from django.urls import path
from . import views

app_name = "susanowo"
urlpatterns = [
    url(r'^$', views.indexviews.login, name='login'),
    url(r'^index/$', views.indexviews.index, name='index'),
    url(r'^inbox/$', views.inboxviews.newInbox, name='inbox'),
    url(r'^inboxupd/$', views.inboxviews.inboxAdd, name='inboxupd'),
    url(r'^modstatus/$', views.indexviews.modstatus, name='modstatus'),
    path('inbox/<int:todo_id>', views.inboxviews.inbox, name='inbox'),
    path('inboxupd/<int:todo_id>', views.inboxviews.inboxUpd, name='inboxupd'),
    url(r'^gomibako/$', views.gomiviews.gomibakoList, name='gomibako'),
    url(r'^gomisakujo/$', views.gomiviews.gomiSakujo, name='gomisakujo'),
    # path('shiryou/<int:todo_id>', views.shiryouviews.shiryouList, name='shiryou'),
    path('shiryou/<int:todo_id>', views.shiryouviews.multi_upload_with_model, name='shiryou'),
    # path('shiryouupd/<int:todo_id>', views.shiryouviews.shiryouupd, name='shiryouupd'),
]
