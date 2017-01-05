#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

import os,sys
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Stark.settings")    #设置系统的环境变量，相当于linux的命令行环境变量
    BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #print(BASE_DIR)
    sys.path.append(BASE_DIR)
    from Arya.action_list import actions    #导入模块
    from Arya.backends.utils import ArgvManagement
    obj = ArgvManagement(sys.argv)