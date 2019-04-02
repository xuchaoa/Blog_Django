#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Archerx
# @time: 2019/3/26 下午 08:34

from django.core.mail import send_mail
from MySite.settings import DEFAULT_FROM_EMAIL

if __name__ == '__main__':

    send_mail('hi','hello world','755563428@qq.com',['1920206224@qq.com'],fail_silently=False)