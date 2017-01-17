#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"


# from django.contrib.auth.models import User
from Sansa import models
from rest_framework import serializers, viewsets, routers

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('url', 'email', 'name', 'is_staff')


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Asset
        depth = 2
        fields = ('url', 'asset_type','sn', 'manufactory','name', 'create_date')


class ManufactorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Manufactory
        fields = ('url', 'manufactory','support_num', 'memo')