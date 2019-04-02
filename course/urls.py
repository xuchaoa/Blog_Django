#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Archerx
# @time: 2019/4/2 上午 10:27

from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'course'

urlpatterns = [
    #path('about/',TemplateView.as_view(template_name='course/about.html')),  #直接返回template不经过view（类模板文件）
    path('about/',views.AboutView.as_view(),name='about'),  #或者这样，继承父类，赋值变量
    path('course_list/',views.CourseListView.as_view(),name='course_list'),

]