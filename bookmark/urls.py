"""mysite path Configuration

The `pathpatterns` list routes paths to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/paths/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a path to pathpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a path to pathpatterns:  path('', Home.as_view(), name='home')
Including another pathconf
    1. Add an import:  from blog import paths as blog_paths
    2. Import the include() function: from django.conf.paths import path, include
    3. Add a path to pathpatterns:  path('blog/', include(blog_paths))
"""
from bookmark.views import *
from . import views
from django.urls import path

app_name = 'bookmark'
urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'),

    path('bookmark2/', BookmarkLV2.as_view(), name='index2'),

    path('(?P<pk>\d+)/', BookmarkDV.as_view(), name='detail'),

    # Example: /add/
    path('add/',
        BookmarkCreateView.as_view(), name="add",
    ),

    # Example: /change/
    path('change/',
        BookmarkChangeLV.as_view(), name="change",
    ),

    # Example: /99/update/
    path('(?P<pk>[0-9]+)/update/',
        BookmarkUpdateView.as_view(), name="update",
    ),

    # Example: /99/delete/
    path('(?P<pk>[0-9]+)/delete/',
        BookmarkDeleteView.as_view(), name="delete",
    ),
]
