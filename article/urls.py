#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Archerx
# @time: 2019/3/27 下午 10:07

from django.urls import path,re_path
from . import views
from . import list_views

app_name = "article"

urlpatterns = [
    path('article_column/',views.article_column,name='article_column'),
    path('rename_column/',views.rename_article_column,name='rename_article_column'),
    path('del_column/',views.del_article_column,name='del_article_column'),
    path('article_post/',views.article_post,name='article_post'),
    path('article_list/',views.article_list,name='article_list'),
    re_path('article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.article_detail, name="article_detail"),
    path('del_article/', views.del_article, name="del_article"),
    path('redit_article/<int:article_id>/', views.redit_article, name="redit_article"),
    path('list_article_titles/', list_views.article_titles, name="article_titles"),
    path('list_article_titles/<username>/', list_views.article_titles, name="author_articles"),
    re_path('list_article_detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', list_views.article_detail, name="list_article_detail"),
    path('like_article/',list_views.like_article,name='like_article'),
    path('article_tag/',views.article_tag,name='article_tag'),
    path('del_article_tag/',views.del_article_tag,name='del_article_tag'),
    path('test/',views.test),
]