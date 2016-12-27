#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"


from Arya.backends.base_module import BaseSaltModule

class User(BaseSaltModule):
    """
    被继承的类，如果操作系统中包含其中的方法，就不再写了，如果没有，就写
    """
    def uid(self):
        pass

    def gid(self):
        pass

    def shell(self):
        pass

    def home(self):
        pass

class UbuntuUser(User):

    def home(self):
        print('in ubuntu home')
