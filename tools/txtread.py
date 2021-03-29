#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/3/1 15:44
#导包
import sys
import os
#当前文件目录
project_path = os.path.dirname(os.path.realpath(__file__))
print(project_path)
sys.path.append(project_path+"\\config")
print(sys.path)
#导入配置文件的模块
from config import config
import pymysql
import codecs
import csv
#定义数据库链接
print(config.server)
def get_conn():
    conn = pymysql.Connect(host=config.server,
                       port=config.port,
                       database=config.database1,
                       user=config.userid,
                       password=config.pwd,
                       autocommit=True
                       )
    return conn
#定义脚本执行，返回元组z
def sql_exwcute(oursor,sql,arg):
    oursor.execute(sql,arg)
    return oursor.fetchall()
#
def read_mysql_csv(filename):
    with codecs.open(filename=filename,mode='w',encoding='utf-8') as f:
        try:
            write = csv.writer(f,dialect='excel')
            write.writerow(['用户名称','用户账号'])
            conn= get_conn()
            cur= conn.cursor()
            sql = 'SELECT UserCode,UserName from uc_tuserbase'
            users= sql_exwcute(cur,sql,arg=None)
        except Exception as e:
            print(e)
        for user in users:
            print(user)
            write.writerow(user)
read_mysql_csv("./userbase.csv")