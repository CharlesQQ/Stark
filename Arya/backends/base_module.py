#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

class BaseSaltModule(object):
    """
    被模块继承,获取主机信息
    """
    def __init__(self,sys_argvs,db_models):
        self.db_models=db_models
        self.sys_argvs=sys_argvs
        self.fetch_hosts()


    def fetch_hosts(self):
        print('--fetch hosts---')
        if '-h' in self.sys_argvs or '-g' in self.sys_argvs:
            if '-h' in self.sys_argvs:
                host_str_index = self.sys_argvs.index('-h')+1
                if len(self.sys_argvs)  <= host_str_index:
                    exit("host argument must be provided after -h")
                else: #get host str   模糊匹配
                    host_str = self.sys_argvs[host_str_index]
                    host_str_list = host_str.split(',')
                    host_list = self.db_models.Host.objects.filter(hostname__in=host_str_list)
                    print("--host list:",host_list)


        else:
            exit("host [-h] or group [-g] agument must be provided")