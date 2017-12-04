from django.conf.urls import url

from . import views
from polls.views import *

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^polls/add/$',
        PollsCreateView.as_view(), name="polls_add",
    ),

    url(r'^polls/change/$',
        PollsChangeLV.as_view(), name="polls_change",
    ),

    url(r'^polls/(?P<pk>[0-9]+)/update/$',
        PollsUpdateView.as_view(), name="polls_update",
    ),

    url(r'^polls/(?P<pk>[0-9]+)/delete/$',
        PollsDeleteView.as_view(), name="polls_delete",
    ),
]
