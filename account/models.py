from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)   #和User表一对一关系
    birth = models.DateField(blank=True,null=True)
    phone = models.CharField(max_length=20,null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)

class UserInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    school = models.CharField(max_length=100,blank=True)
    company = models.CharField(max_length=100,blank=True)
    profession = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=100,blank=True)
    aboutme = models.TextField(blank=True)
    # photo = models.ImageField(blank=True)  #可以为空
    photo = models.TextField(blank=True)  #上面sql由于长度问题，上传图片会报错
    def __str__(self):
        return 'user: {}'.format(self.user.username)