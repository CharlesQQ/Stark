#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"


from Arya.backends.base_module import BaseSaltModule
"""
根据输入的主机，判断是否有与该主机匹配的操作系统的类，如果有，实例化子类，没有实例化父类就；也就是根据不同的输入，实例化不同的类，类似于工厂模式;
"""

class User(BaseSaltModule):
    """
    被继承的类，如果操作系统中包含其中的方法，就不再写了，如果没有，就写
    """
    def uid(self,*args,**kwargs):
        self.argv_validation('uid',args[0],int)  #监测语法的合法性
        cmd = "-u %s" %args[0]
        self.raw_cmds.append(cmd)
        return cmd

    def gid(self,*args,**kwargs):
        self.argv_validation('gid',args[0],int)  #监测语法的合法性
        cmd = "-g %s" %args[0]
        self.raw_cmds.append(cmd)
        return cmd

    def shell(self,*args,**kwargs):
        self.argv_validation('shell',args[0],str)  #监测语法的合法性
        cmd = "-s %s" %args[0]
        self.raw_cmds.append(cmd)
        return cmd

    def home(self,*args,**kwargs):
        self.argv_validation('home',args[0],str)  #监测语法的合法性
        cmd = "-d %s" %args[0]
        self.raw_cmds.append(cmd)
        return cmd

    def present(self,*args,**kwargs):    #将上述内容组合起来
        cmd_list = []
        username = kwargs.get('section')
        # print(username)
        # print("raw cmds:",self.raw_cmds)
        # print("single_line_cmds",self.single_line_cmds)
        self.raw_cmds.insert(0,"useradd %s" %username)
        cmd_list.append(' '.join(self.raw_cmds))
        cmd_list.extend(self.single_line_cmds)
        print("cmd list:",cmd_list)

    def is_required(self,*args,**kwargs):
        print('checking user required',args,kwargs)


class UbuntuUser(User):

    # def home(self,*args,**kwargs):
    #     print('in ubuntu home')

    def password(self,*args,**kwargs):
        username=kwargs.get('section')
        password=args[0]

        cmd = '''echo "%s:%s"  |sudo chpasswd ''' %(username,password)
        self.single_line_cmds.append(cmd)
