#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"


from Arya.backends.base_module import BaseSaltModule

class Group(BaseSaltModule):

    def gid(self,*args,**kwargs):
        pass

    def present(self,*args,**kwargs):
        pass

    def is_required(self,*args,**kwargs):
        name = args[1]

        cmd = '''more /etc/group |awk -F ':' '{print $1}' |grep -w %s -q;echo $?''' %name
        return cmd