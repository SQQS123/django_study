﻿"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-0*&t*o!_&r+ty@)t51kg&l@dy!x!4en59lnyiw1y5^%8dal86'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'Recent_Read',
    'Run',
    'Ajax',
    'Like',
    'Attitude',
    'Comment',
    'ckeditor',
    'Send_Email',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_PATH = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (
        STATIC_PATH,
     )

# 文件上传设置

# 指定上传文件的存放目录
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# 用于设置访问文件的url，后面访问时会用到。
MEDIA_URL = '/media/'


# CKEDITOR相关设置
CKEDITOR_CONFIGS = {
     'comment_ckeditor': {
         'toolbar': 'custom',
         'toolbar_custom':[
             ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
             ['TextColor', 'BGColor', 'RemoveFormat'],
             ['NumberedList', 'BulletedList'],
             ['Link', 'Unlink'],
             [ 'SpecialChar', 'Blockquote'],
             ],
            'width': 'auto',
            'height': '180',
            'tabSpaces': 4,
            'removePlugins': 'elementspath',
            'resize_enabled': False,
         }
}


# 发送邮件设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# SMTP地址
EMAIL_HOST = 'smtp.qq.com'
# SMTP端口
EMAIL_PORT = 465
# 自己的邮箱
EMAIL_HOST_USER = '2551628690@qq.com'
# 自己的邮箱授权码，非密码
EMAIL_HOST_PASSWORD = 'xxxxxxxx'
EMAIL_SUBJECT_PREFIX = '[黄文杨的博客]'
# 与SMTP服务器通信时，是否启动TLS链接(安全链接)。默认是false
EMAIL_USE_SSL = True



