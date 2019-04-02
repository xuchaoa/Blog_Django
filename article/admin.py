from django.contrib import admin
from .models import ArticleColumn

# Register your models here.


class ArticleColumnAdmin(admin.ModelAdmin):  #定义管理后台视图
    list_display = ('column','create','user')
    list_filter = ('column',)

admin.site.register(ArticleColumn,ArticleColumnAdmin)
