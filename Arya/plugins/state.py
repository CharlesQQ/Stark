#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

from Arya.backends.base_module import BaseSaltModule
import os

class State(BaseSaltModule):

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
                yaml_file_path = "%s/%s" %(self.settings.SALT_CONFIG_FILES_DIR,yaml_filename)
                if os.path.isfile(yaml_file_path):
                    pass
            except Exception,e:
