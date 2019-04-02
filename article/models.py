from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from slugify import slugify
# Create your models here.

class ArticleColumn(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='article_column')  #外键，代表一对多关系
    column = models.CharField(max_length=200)
    create = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return self.column


class ArticleTag(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='tag')
    tag = models.CharField(max_length=500)

    def __str__(self):
        return self.tag

class ArticlePost(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='article')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    column = models.ForeignKey(ArticleColumn,on_delete=models.CASCADE, related_name='article')
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)   #对应setting.py 中的配置如下：TIME_ZONE = 'Asia/Shanghai'
    updated = models.DateTimeField(auto_now=True)
    users_like = models.ManyToManyField(User,related_name='articles_like',blank=True)  #多对多关系,会新建一张表存储对应关系,只需要在一个类中声明一个字段即可
    article_tag = models.ManyToManyField(ArticleTag,related_name='article_tag')
    class Meta:
        ordering = ('title',)
        index_together = (('id','slug'),) #对这两个对象建立索引

    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(ArticlePost,self).save(*args,**kwargs)
    def get_absolute_url(self):
        return reverse('article:article_detail',args=[self.id,self.slug])
    def a(self):
        return reverse('article:list_article_detail',args=[self.id,self.slug])



class Comment(models.Model):
    article = models.ForeignKey(ArticlePost,on_delete=models.CASCADE,related_name='comments')
    commentator = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return "comment by {} on {}".format(self.commentator.username,self.article)


