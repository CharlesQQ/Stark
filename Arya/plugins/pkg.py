#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"


from Arya.backends.base_module import BaseSaltModule

class Pkg(BaseSaltModule):
    pass

    def is_required(self,*args,**kwargs):
        return 'echo 0'