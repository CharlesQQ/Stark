#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

from Arya import action_list

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
        print(self.argvs)
        if len(self.argvs) <2:
            self.help_msg()
        module_name=self.argvs[1]
        if '.' in module_name:
            mod_name,mod_method=module_name.split('.')
            module_instance=action_list.actions.get(module_name)
            if module_instance: #matched
                module_instance(self.argvs)

        else:
            exit("Invalid module name argument")
