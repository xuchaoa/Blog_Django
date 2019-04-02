#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Archerx
# @time: 2019/3/25 下午 04:41


from django import forms
from django.contrib.auth.models import User
from .models import UserProfile,UserInfo

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# ins = LoginForm()
# dir(ins)    #查看对象的一些属性

class RegisterForm(forms.ModelForm):  #继承了forms.Form
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Pssword", widget=forms.PasswordInput)
    # phone = forms.CharField(max_length=20,null=True)

    class Meta:
        model = User
        fields = ("username", "email")

    def clean_password2(self):  #暂时无用
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("passwords do not match.")
        return cd['password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone','birth')

class UserInfoForm(forms.ModelForm):
    class Meta:  #内部类/元类
        model = UserInfo
        fields = ('school','company','profession','address','aboutme','photo')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)