#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

from django.conf.urls import url,include


from Arya import views
urlpatterns = [

    url(r'file_center/',views.file_download),
]