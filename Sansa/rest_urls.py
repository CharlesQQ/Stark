#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"


from django.conf.urls import url, include
from rest_framework import routers

from  Sansa import rest_views
router = routers.DefaultRouter()
router.register(r'users', rest_views.UserViewSet)    #生成一条url
router.register(r'assets', rest_views.AssetViewSet)    #生成一条url
router.register(r'manufactory', rest_views.ManufactoryViewSet)    #生成一条url


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]