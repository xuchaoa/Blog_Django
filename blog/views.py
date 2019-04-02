from django.shortcuts import render,get_object_or_404

from .models import BlogArticles
# Create your views here.

def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request,"blog/titles.html",{'blogs':blogs})



def blog_article(request,id):
    article = get_object_or_404(BlogArticles,id=id)   #生产模式防止404敏感信息显示
    dic_info = {
        'article':article,
        'publish':article.publish
    }

    return render(request,'blog/content.html',dic_info)