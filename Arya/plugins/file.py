#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"


from Arya.backends.base_module import BaseSaltModule

class File(BaseSaltModule):
    """
      file.managed:
        - source: salt://apache/httpd.conf
        - user: root
        - group: root
        - mode: 644
        - require:
          - pkg: nginx
    """

    def managed(self,*args,**kwargs):
        print("manage...",args,kwargs)
        kwargs['sub_action']='managed'
        return kwargs

    def source(self,*args,**kwargs):
        pass

    def user(self,*args,**kwargs):
        pass

    def group(self,*args,**kwargs):
        pass

    def mode(self,*args,**kwargs):
        pass

    def is_required(self,*args,**kwargs):
        file_path = args[1]
        cmd = "test -f %s;echo $?" %file_path
        return cmd
