#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

from Arya.backends.base_module import BaseSaltModule
import os

class State(BaseSaltModule):


    def load_state_files(self,state_filename):   #解析yaml文件
        from yaml import load,dump
        try:
            from  yaml import CLoader as Loader,CDumper as  Dumper
        except ImportError:
            from yaml import Loader,Dumper
        state_file_path = "%s/%s" %(self.settings.SALT_CONFIG_FILES_DIR,state_filename)
        if os.path.isfile(state_file_path):
            with open(state_file_path) as f:
                data = load(f.read(),Loader=Loader)
                return data
        else:
            exit("%s is not a valid file" %state_file_path )


    def apply(self):
        """
        1、load the configurations file
        2、parse it
        3、create a task and send it to MQ
        4、collect the result with task-callback id
        :return:
        """

        if '-f' in self.sys_argvs:
            yaml_file_index = self.sys_argvs.index('-f') + 1
            try:
                yaml_filename = self.sys_argvs[yaml_file_index]
                state_data = self.load_state_files(yaml_filename)
                print('state data:',state_data)

                for os_type,os_type_data in self.config_data_dic.items():    #按照不同的操作系统生成单独的配置文件

                    for section_name,section_data in state_data.items():
                        print('Section:',section_name)
                        for mod_name,mod_data in section_data.items():
                            base_mod_name = mod_name.split(".")[0]
                            plugin_file_path = "%s/%s.py" %(self.settings.SALT_PLUGINS_DIR,base_mod_name)
                            if os.path.isfile(plugin_file_path):
                                #导入模块
                                module_plugin = __import__('Arya.plugins.%s' %base_mod_name)
                                special_os_module_name = "%s%s" %(os_type.capitalize(),base_mod_name)
                                print("dir module plugin:",module_plugin)
                                getattr(module_plugin,base_mod_name)   #真正导入模块
                                if hasattr(module_plugin,special_os_module_name):    #判断有没有根据操作系统的类型进行特殊解析的类，在这个文件中
                                    module_instance = getattr(module_plugin,special_os_module_name)
                                else:
                                    module_instance = getattr(module_plugin,base_mod_name)
                                #开始调用此module，进行配置解析
                                module_obj = module_instance(self.sys_argvs,self.db_models,self.settings)      #所有的模块都需要参数，因为都继承了父类
                            else:
                                exit("module [%s] is not exist" %base_mod_name)
                            print("  ",mod_name)

                            for state_item in mod_data:
                                print("\t",state_item)      #输出yaml的格式
            except IndexError as e:
                exit("state file must be provided after -f")
        else:
            exit("state file must be specified")
