"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url('', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url('blog/', include(blog_urls))
"""

from blog.views import *
from django.urls import path

app_name = 'blog'
urlpatterns = [

    # Example: /

    path('', PostLV.as_view(), name='index'),

    path('post2/', PostLV2.as_view(), name='index2'),

    # Example: /post/ (same as /)
    path('post/', PostLV.as_view(), name='post_list'),

    # Example: /post/django-example/
    path('post/(?P<slug>[-\w]+)/', PostDV.as_view(), name='post_detail'),

    # Example: /archive/
    path('archive/', PostAV.as_view(), name='post_archive'),

    # Example: /2012/
    path('(?P<year>\d{4})/', PostYAV.as_view(), name='post_year_archive'),

    # Example: /2012/nov/
    path('(?P<year>\d{4})/(?P<month>[a-z]{3})/', PostMAV.as_view(), name='post_month_archive'),

    # Example: /2012/nov/10/
    path('(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/', PostDAV.as_view(), name='post_day_archive'),

    # Example: /today/
    path('today/', PostTAV.as_view(), name='post_today_archive'),

    # Example: /tag/
    path('tag/', TagTV.as_view(), name='tag_cloud'),

    # Example: /tag/tagname/
    path('tag/(?P<tag>[^/]+(?u))/', PostTOL.as_view(), name='tagged_object_list'),

    # Example: /search/
    path ('search/', SearchFormView.as_view(), name='search'),

    # Example: /add/
    path('add/',
        PostCreateView.as_view(), name="add",
    ),

    # Example: /change/
    path('change/',
        PostChangeLV.as_view(), name="change",
    ),

    # Example: /99/update/
    path('(?P<pk>[0-9]+)/update/',
        PostUpdateView.as_view(), name="update",
    ),

    # Example: /99/delete/
    path('(?P<pk>[0-9]+)/delete/',
        PostDeleteView.as_view(), name="delete",
    ),

    # Example: /test/
    #path('test/', TestPostLV.as_view(), name='post_test'),
    # Example: /test/word/
    path('test/(?P<word>[\w]+)/', TestPostLV.as_view(), name='post_test'),
]
