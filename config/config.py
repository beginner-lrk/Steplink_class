#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/3/1 15:44
#导包
import configparser
import os
#用户os模块先读取当前文件路径
'''
写法1：
path =os.getcwd()
configfile = os.path.abspath(path)
'''
configfile = os.path.dirname(os.path.realpath(__file__))
#读取本地的配置文件地址
cfgfile = os.path.join(configfile,"config.ini")
#print(cfgfile)
#实例化调用读取配置模块中的类
conf = configparser.ConfigParser()
conf.read(cfgfile,encoding='utf-8')
#调用get方法，然后获取配置的数据
server = conf.get("connect_mysql", "server")
port = int(conf.get("connect_mysql", "port"))
userid = conf.get("connect_mysql", "userid")
pwd = conf.get("connect_mysql", "password")
database = conf.get("connect_mysql", "database")
database1 = conf.get("connect_mysql", "database1")
print(server,port,userid,pwd,database)
# email_on = conf.get("EMAIL", "on_off")
# email_subject = int(conf.get("EMAIL", "subject"))
# email_app = conf.get("EMAIL", "app")
# email_addressee = conf.get("EMAIL", "addressee")
# email_ccaddressee = conf.get("EMAIL", "ccaddressee")