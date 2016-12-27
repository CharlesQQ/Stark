#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

from Arya import action_list
import django
django.setup()    #将django的环境变量加载进来,必须先加载app

from Stark import settings
from Arya import models

class ArgvManagement(object):
    """
    接收用户指令并分配到相应的模块
    """
    def __init__(self,argvs):
        self.argvs=argvs
        self.argv_parse()

    def help_msg(self):
        print("Available modules")
        for registered_module in action_list.actions:
            print("\t%s" %registered_module)
        exit()

    def argv_parse(self):
        #print(self.argvs)
        if len(self.argvs) <2:
            self.help_msg()
        module_name=self.argvs[1]
        if '.' in module_name:
            mod_name,mod_method=module_name.split('.')
            module_instance=action_list.actions.get(mod_name)
            if module_instance: #matched
                module_obj = module_instance(self.argvs,models,settings)
                if hasattr(module_obj,mod_method):
                    module_method_obj = getattr(module_obj,mod_method)
                    module_method_obj()  #调用指定的指令
                    #module_method_obj.process()    #解析任务，发送到队列，取任务结果
                else:
                    exit("module [%s] doesn't have [%s] method" %(mod_name,mod_method))

        else:
            exit("Invalid module name argument")
