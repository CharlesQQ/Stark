#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

import os
class BaseSaltModule(object):
    """
    被模块继承,获取主机信息
    """
    def __init__(self,sys_argvs,db_models,settings):
        self.db_models = db_models
        self.settings =  settings
        self.sys_argvs=sys_argvs
        # self.fetch_hosts()    #获取主机列表
        # self.config_data_dic = self.get_selected_os_types()

    def argv_validation(self,argv_name,val,data_type):
        if type(val) is not data_type:
            exit("Erro:[%s]'s data type is not valid" %argv_name)

    def get_selected_os_types(self):
        """
        获取操作系统类型
        :return:
        """
        data = {}
        for host in self.host_list:
            data[host.os_type] = []
        print('-->data',data)
        return data

    def process(self):    #抽象类
        self.fetch_hosts()    #获取主机列表,self.host_list
        self.config_data_dic = self.get_selected_os_types()    #通过host_list列举出对于的os的类型


    def require(self,*args,**kwargs):
        print("in require",args,kwargs)
        os_type = kwargs.get('os_type')

        self.require_list = []
        for item in args[0]:
            for mod_name,mod_val in item.items():
                module_obj = self.get_module_instance(base_mod_name=mod_name,os_type=os_type)
                require_condition = module_obj.is_required(mod_name,mod_val)
                self.require_list.append(require_condition)
                # print("require run module:",module_obj)
        # print("require list",self.require_list)


    def fetch_hosts(self):
        print('--fetch hosts---')
        if '-h' in self.sys_argvs or '-g' in self.sys_argvs:
            host_list = []
            if '-h' in self.sys_argvs:
                host_str_index = self.sys_argvs.index('-h')+1
                if len(self.sys_argvs)  <= host_str_index:
                    exit("host argument must be provided after -h")
                else: #get host str   模糊匹配
                    host_str = self.sys_argvs[host_str_index]
                    host_str_list = host_str.split(',')
                    host_list += self.db_models.Host.objects.filter(hostname__in=host_str_list)
                    #print("--host list:",host_list)

            if '-g' in self.sys_argvs:
                group_str_index = self.sys_argvs.index('-g')+1
                if len(self.sys_argvs)  <= group_str_index:
                    exit("host argument must be provided after -h")
                else: #get host str   模糊匹配
                    group_str = self.sys_argvs[group_str_index]
                    group_str_list = group_str.split(',')
                    group_list = self.db_models.HostGroup.objects.filter(name__in=group_str_list)
                    for group in group_list:
                        host_list +=group.hosts.select_related()
            self.host_list = set(host_list)
            return True

        else:
            exit("host [-h] or group [-g] agument must be provided")



    def is_required(self,*args,**kwargs):     #基类中的方法，啥也不做，如果子类中没有这个方法，退出，后面的不执行
        exit('Error: is_required() method must be implemented in module class [%s]'%args[0])

    def get_module_instance(self,*args,**kwargs):
        base_mod_name = kwargs.get('base_mod_name')   #user
        os_type = kwargs.get('os_type')
        plugin_file_path = "%s/%s.py" % (self.settings.SALT_PLUGINS_DIR, base_mod_name)       #plugins/user.py
        if os.path.isfile(plugin_file_path):
            # 导入模块
            module_plugin = __import__('plugins.%s' % base_mod_name)  # 导入plugins整个包     #plugin.user
            # print(module_plugin)
            special_os_module_name = "%s%s" % (os_type.capitalize(), base_mod_name.capitalize())    #UbuntuUser
            module_file = getattr(module_plugin, base_mod_name)  # 真正导入模块      plugin user
            if hasattr(module_file, special_os_module_name):  # 判断有没有根据操作系统的类型进行特殊解析的类，在这个文件中;比如在user.py中看
                module_instance = getattr(module_file, special_os_module_name)  # 导入类
            else:
                module_instance = getattr(module_file, base_mod_name.capitalize())
            module_obj = module_instance(self.sys_argvs, self.db_models, self.settings)   #实例化UbuntuUser
            return module_obj

    def  syntax_parser(self,section_name,mod_name,mod_data,os_type):    #每个类都需要进行解析      apache/user.present ...
        print("--going to parser state data:",section_name,mod_name)

        self.raw_cmds = []
        self.single_line_cmds = []
        for state_item in mod_data:
            print("\t",state_item)
            for key,val in state_item.items():
                if hasattr(self,key):      #是否有shell/passord等方法
                    # print(key)
                    state_func = getattr(self,key)
                    state_func(val,section=section_name,os_type=os_type)
                else:
                    exit("Error:module [%s] has no argument %s+++" %(mod_name,key))
        else:    #for循环不break，就执行else
            if '.' in mod_name:
                base_mod_name,mod_action = mod_name.split('.')
                if hasattr(self,mod_action):
                    mod_action_func = getattr(self,mod_action)
                    cmd_list = mod_action_func(section=section_name,mod_data=mod_data)          #present
                    data = {
                        'cmd_list':cmd_list,
                        'require_list':self.require_list,
                    }
                    #上面代表一个section里面的一个module已经解析完毕了

                    if type(cmd_list) is dict:
                        data['file_module'] = True
                        data['sub_action'] = cmd_list.get('sub_action')
                    return data
                else:
                    exit("Error:module [%s] has no argument %s---" %(mod_name,mod_action))
            else:
                exit("Error:module action of [%s] must be supplied" %(mod_name))
