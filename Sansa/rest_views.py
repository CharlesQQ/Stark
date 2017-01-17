#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

from Sansa import models
from Sansa import serializer

from rest_framework import serializers, viewsets, routers


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializer.UserSerializer

class AssetViewSet(viewsets.ModelViewSet):
    queryset = models.Asset.objects.all()
    serializer_class = serializer.AssetSerializer


class ManufactoryViewSet(viewsets.ModelViewSet):
    queryset = models.Manufactory.objects.all()
    serializer_class = serializer.ManufactorySerializer