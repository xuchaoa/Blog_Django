#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Archerx
# @time: 2019/3/31 下午 07:53


# 自定义模板标签文件

from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe  #类似于html实体化
import markdown


register = template.Library()
from article.models import ArticlePost

@register.simple_tag()
def total_articles():
    return ArticlePost.objects.count()

@register.simple_tag()
def author_total_articles(user):
    return user.article.count()  #因为model中设置了外键和related_name

@register.inclusion_tag('article/list/latest_articles.html')
def latest_articles(n=5):
    latest_articles = ArticlePost.objects.order_by('-created')[:n]
    return {'latest_articles':latest_articles}

@register.simple_tag()
def most_commented_articles(n=3):
    return ArticlePost.objects.annotate(total_comments=Count("comments")).order_by("-total_comments")[:n]

@register.filter(name='markdown')  #重命名下面的选择器函数为markdown
def markdown_filter(text):
    return mark_safe(markdown.markdown(text))