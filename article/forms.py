#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Archerx
# @time: 2019/3/27 下午 09:57

from django import forms
from .models import ArticleColumn,ArticlePost,Comment,ArticleTag

class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ('column',)

class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ('title','body')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('commentator','body',)


class ArticleTagForm(forms.ModelForm):
    class Meta:
        model = ArticleTag
        fields = ('tag',)