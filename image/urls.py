#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Archerx
# @time: 2019/4/1 下午 09:34
from django.urls import path
from . import views

app_name = 'image'

urlpatterns = [
    path('list_images/', views.list_images, name="list_images"),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('del_image/', views.del_image, name='del_image'),
    path('images/',views.falls_images,name='falls_images')

]