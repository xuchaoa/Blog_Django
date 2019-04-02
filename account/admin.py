from django.contrib import admin
from .models import UserProfile,UserInfo
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','birth','phone')  #列出那些项目
    list_filter = ('phone',)   #单元素tuple加逗号，防止歧义  #定义右上角过滤器显示的内容


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user','school','company','profession','address','aboutme','photo')
    list_filter = ('school','company','profession')

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(UserInfo,UserInfoAdmin)