#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Archerx
# @time: 2019/3/29 下午 05:07

from django.shortcuts import render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import ArticlePost,ArticleColumn
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import redis
from django.conf import settings
from .forms import CommentForm
from django.db.models import Count

def article_titles(request,username=None):
    if username:
        user = User.objects.get(username=username)
        articles_title = ArticlePost.objects.filter(author=user)
        try:
            userinfo = user.userinfo
        except:
            userinfo = None
    else:
        articles_title = ArticlePost.objects.all()
    paginator = Paginator(articles_title,3)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        articles = current_page.object_list
    except PageNotAnInteger:  # 页码不是整数
        current_page = paginator.page(1)
        articles = current_page.object_list
    except EmptyPage:  # 页码是空
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list
    if username:
        return render(request, 'article/list/author_articles.html', {'articles': articles,
                                                                'page': current_page,
                                                                'userinfo':userinfo,'user':user})
    else:
        return render(request, 'article/list/article_titles.html', {'articles': articles,
                                                                    'page': current_page})

def article_detail(request,id,slug):
    con = redis.StrictRedis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=settings.REDIS_DB)
    article = get_object_or_404(ArticlePost,id=id,slug=slug)
    total_views = con.incr('article:{}:views'.format(article.id))  #增加键值并返回当前值
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
    else:
        comment_form = CommentForm()

    article_tags_ids = article.article_tag.values_list('id',flat=True)
    similar_articles = ArticlePost.objects.filter(article_tag__in=article_tags_ids).exclude(id=article.id)
    similar_articles = similar_articles.annotate(same_tag=Count('article_tag')).order_by('-same_tag','-created')[:4]
    return render(request,'article/list/article_detail.html',{'article':article,'total_views':total_views,
                                                              'comment_form':comment_form,'similar_articles':similar_articles})


@csrf_exempt
@require_POST
@login_required(login_url='/account/login/')
def like_article(request):
    article_id = request.POST.get('id')
    action = request.POST.get('action')
    if article_id and action:
        try:
            article = ArticlePost.objects.get(id=article_id)
            if action == 'like':
                article.users_like.add(request.user)
                return HttpResponse('1')
            elif action == 'unlike':
                article.users_like.remove(request.user)
                return HttpResponse('2')
            else:
                return HttpResponse('3')
        except:
            return HttpResponse('4')


