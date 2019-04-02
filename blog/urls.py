#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Archerx
# @time: 2019/3/24 下午 04:17

from django.urls import path
from . import views


app_name = "blog"  #指定app的名称，否则会报错

urlpatterns = [
    path("",views.blog_title,name='blog_title'),
    path('<int:id>/',views.blog_article,name='blog_details'),
]