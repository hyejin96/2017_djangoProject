
from django.urls import path
from . import views
from polls.views import *

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('(?P<pk>[0-9]+)/', views.DetailView.as_view(), name='detail'),
    path('(?P<pk>[0-9]+)/results/', views.ResultsView.as_view(), name='results'),
    path('(?P<question_id>[0-9]+)/vote/', views.vote, name='vote'),
    path('polls/add/',
        PollsCreateView.as_view(), name="polls_add",
    ),

    path('polls/change/',
        PollsChangeLV.as_view(), name="polls_change",
    ),

    path('polls/(?P<pk>[0-9]+)/update/',
        PollsUpdateView.as_view(), name="polls_update",
    ),

    path('polls/(?P<pk>[0-9]+)/delete/',
        PollsDeleteView.as_view(), name="polls_delete",
    ),
]
