#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Archerx
# @time: 2019/3/25 下午 04:35

from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy #防止硬编码


app_name = 'account'


urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='account/login2.html'),name='auth_login'),
    # path('login/',views.user_login,name='auth_login'),
    # path('login/',auth_views.LoginView.as_view(template_name='account/login2.html'),name = 'auth_login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='account/logout.html'),name = 'auth_logout'),
    path('register/',views.register,name = 'user_register'),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='account/password_change_form.html',
                                                                  success_url=reverse_lazy('account:auth_passwordchange_done')),name = 'auth_passwordchange'),
    path('password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'),name = 'auth_passwordchange_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="account/password_reset_form.html",
                                                                 email_template_name="account/password_reset_email.html",
                                                                 success_url=reverse_lazy('account:password_reset_done')),name='password_reset'),
    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html",
                                                     success_url=reverse_lazy('account:password_reset_down')),name="password_reset_confirm"),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),
    path('my_information/',views.myself,name='my_information'),
    path('edit_my_information/',views.myself_edit,name='my_information_edit'),
    path('my_image/',views.my_image,name='my_image')

]