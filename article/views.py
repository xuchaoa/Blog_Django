from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ArticleColumn,ArticlePost,ArticleTag
from .forms import ArticleColumnForm,ArticlePostForm,ArticleTagForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST,require_GET
from django.http import HttpResponse
from django.shortcuts import get_object_or_404  #一般在展示文章时候使用
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger   #内置分页函数
import json
# Create your views here.

@login_required(login_url='/account/login/')
@csrf_exempt
def article_column(request):
    if request.method == 'GET':
        columns = ArticleColumn.objects.filter(user_id=request.user.id)
        column_form = ArticleColumnForm()
        return render(request,'article/column/article_column.html',{'columns':columns,'column_form':column_form})
    if request.method == 'POST':
        column_name = request.POST.get('column')
        columns = ArticleColumn.objects.filter(user_id=request.user.id,column=column_name)
        if columns:
            return HttpResponse('have exist')
        else:
            ArticleColumn.objects.create(user_id=request.user.id,column=column_name)
            return HttpResponse('success')


@login_required(login_url='/account/login')
@require_POST   #只接受POST数据
@csrf_exempt
def rename_article_column(request):
    column_name = request.POST['column_name']
    column_id = request.POST['column_id']
    try:
        line = ArticleColumn.objects.get(id=column_id,user_id=request.user.id)  #安全问题修复
        line.column = column_name
        line.save()
        return HttpResponse('1')
    except:
        return HttpResponse('0')

@login_required(login_url='account/login')
@require_POST
@csrf_exempt
def del_article_column(request):
    column_id = request.POST.get('column_id')
    try:
        line = ArticleColumn.objects.get(user_id=request.user.id,id=column_id)
        line.delete()
        return HttpResponse(1)
    except:
        return HttpResponse(0)

@login_required(login_url='/account/login')
@csrf_exempt
def article_post(request):
    if request.method == 'POST':
        article_post_form = ArticlePostForm(data=request.POST)  #可以直接用此方法格式化为字典对象
        if article_post_form.is_valid():
            cd = article_post_form.cleaned_data

            try:
                new_article = article_post_form.save(commit=False)
                # 当你通过表单获取你的模型数据，但是需要给模型里其他字段添加一些非表单的数据，该方法会非常有用。
                # 如果你指定commit = False，那么save方法不会理解将表单数据存储到数据库，而是给你返回一个当前对象
                # 。这时你可以添加表单以外的额外数据，再一起存储。
                new_article.author = request.user
                new_article.column = request.user.article_column.get(id=request.POST['column_id'])
                new_article.save()
                tags = request.POST['tag']
                if tags:
                    for atag in json.loads(tags):
                        tag = request.user.tag.get(tag=atag)
                        new_article.article_tag.add(tag)  #关系表新增加一条记录
                return HttpResponse('1')
            except:
                return HttpResponse('2')
        else:
            return HttpResponse('3')
    else:
        article_post_form = ArticlePostForm()
        article_tags = request.user.tag.all()
        article_columns = request.user.article_column.all()   #因为models 外键中的这个参数  related_name='article_column'(可以找到article_column中所有该用户的实例，注意是实例)
        return render(request,'article/column/article_post.html',{'article_post_form':article_post_form,'article_columns':article_columns,
                                                                  'article_tags':article_tags})


@login_required(login_url='/account/login')
def article_list(request):
    articles = ArticlePost.objects.filter(author=request.user)  #request.user是用户名str
    for a in articles:
        print(a.column)  #返回的事ArticleColumn实例
        print(a.column.column)  #实例的字段值
    return render(request,'article/column/article_list.html',{'articles':articles})


@login_required(login_url='/account/login')
@require_GET
def article_detail(request,id,slug):
    article = get_object_or_404(ArticlePost,id=id,slug=slug,author_id=request.user.id)
    return render(request,'article/column/article_detail.html',{'article':article})


@login_required(login_url='/account/login')
@require_POST
@csrf_exempt
def del_article(request):
    article_id = request.POST['article_id']
    try:
        article = ArticlePost.objects.get(id=article_id)
        article.delete()
        return HttpResponse('1')
    except:
        return HttpResponse('2')


@login_required(login_url='/account/login')
@csrf_exempt
def redit_article(request,article_id):
    if request.method == 'GET':
        article_columns = request.user.article_column.all()  #获取ArticleColumn字符串对象集（QuerySet）
        print(article_columns)
        article = ArticlePost.objects.get(id=article_id)    #获取单一article实例
        this_article_form = ArticlePostForm(initial={'title':article.title})   #获取渲染完的表单
        print(article.column)  #算是一个实例，这一列
        print(article.column.column)   #关联到article_column数据库的column字段
        print(type(article.column))  #<class 'article.models.ArticleColumn'>
        print(type(article.column.column))   #<class 'str'>
        this_article_column = article.column
        return render(request,'article/column/redit_article.html',{'article':article,'article_columns':article_columns,'this_article_form':this_article_form,
                                                                   'this_article_column':this_article_column})

    if request.method == 'POST':
        redit_article = ArticlePost.objects.get(id=article_id)
        try:
            redit_article.column = request.user.article_column.get(id=request.POST['column_id']) #?????????
            print(redit_article.column)  #一个ArticleColumn对象   ArticleColumn object (1)
            print(request.user)
            print(request.user.article_column)
            print(request.user.article_column.get(id=request.POST['column_id']))
            redit_article.title = request.POST['title']
            redit_article.body = request.POST['body']
            redit_article.save()
            return HttpResponse("1")
        except:
            return HttpResponse("2")


@login_required(login_url='/account/login')
def article_list(request):
    article_list = ArticlePost.objects.filter(author=request.user)
    paginator = Paginator(article_list,8)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        articles = current_page.object_list
    except PageNotAnInteger:  #页码不是整数
        current_page = paginator.page(1)
        articles = current_page.object_list
    except EmptyPage:  #页码是空
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list
    return render(request,'article/column/article_list.html',{'articles':articles,
                                                              'page':current_page})

@login_required(login_url='/account/login/')
@csrf_exempt    #无法防止csrf
def article_tag(request):
    if request.method == 'GET':
        article_tags = ArticleTag.objects.filter(author=request.user)
        article_tag_form = ArticleTagForm()
        return render(request,'article/tag/tag_list.html',{'article_tags':article_tags,
                                                           'article_tag_form':article_tag_form})
    if request.method == 'POST':
        tag_post_form = ArticleTagForm(request.POST)
        if tag_post_form.is_valid():
            try:
                new_tag = tag_post_form.save(commit=False)
                new_tag.author = request.user
                new_tag.save()
                return HttpResponse('1')
            except:
                return HttpResponse('post data error')
        else:
            return HttpResponse('the form is not valid')

@login_required(login_url='/account/login/')
@csrf_exempt
def del_article_tag(request):
    tag_id = request.POST['tag_id']
    try:
        tag = ArticleTag.objects.get(id=tag_id)
        tag.delete()
        return HttpResponse('1')
    except:
        return HttpResponse('2')


@login_required(login_url='/account/login')
def test(request):
    print(request.user)
    return HttpResponse('this is test page')

