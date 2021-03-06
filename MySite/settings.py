"""
Django settings for BlogDemo project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #获取文件所在目录


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-y$oiu6ppi!tlxc(m)g&b6!2p1b#fqt4%@dydr@icc4(xpex^a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',   #内置用户管理应用
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',   #静态文件引入
    'blog',     #新建立的应用名称
    'account',
    'article',
    'image',
    'sorl.thumbnail',  #缩略图显示
    'course',
]

MIDDLEWARE = [   #中间件
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MySite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]   #定义了模板目录
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MySite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        'NAME': 'blog',         # 你要存储数据的库名，事先要创建之
        'USER': 'blog',         # 数据库用户名
        'PASSWORD': 'blog.Dxxx',     # 密码
        'HOST': '10.6.65.106',    # 主机
        'PORT': '3306',         # 数据库使用的端口

    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'   #每个 APP 目录下的静态资源目录。

STATICFILES_DIRS = [    #用于存放所有应用共用甚至是所有的静态文件，位于整个项目根目录
    os.path.join(BASE_DIR,'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn')   #文件夹收集静态文件用于部署生产环境  $ python manage.py collectstatic



# 静态文件查找顺序
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",   #首先去STATICFILES_DIRS文件夹中查找规定的静态文件
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"   #然后去app目录
)

LOGIN_REDIRECT_URL = '/home/'   #登陆成功之后之后跳转


# 发件邮箱配置
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  #把要发送的邮件显示再控制台上，方便调试
EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST_USER = '15615833854@163.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 465
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# 一般步骤： 编写model -> 编写forms表单类  -> 编写view  ->  编写templeta  -> 设置urls


LOGIN_URL = '/accounts/login/'  # 登陆跳转地址，这个路径需要根据你网站的实际登陆地址来设置

# Redis配置

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

# 图片配置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media/')