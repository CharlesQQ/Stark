#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

class BaseSaltModule(object):
    """
    被模块继承,获取主机信息
    """
    def __init__(self,sys_argvs,db_models,settings):
        self.db_models=db_models
        self.settings =  settings
        self.sys_argvs=sys_argvs
        self.fetch_hosts()    #获取主机列表
        self.config_data_dic = self.get_selected_os_types()

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
        pass


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