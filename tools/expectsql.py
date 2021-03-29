#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/3/15 16:26
import sys
import os

path_sys = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path_sys + "\\config")
from config import config
import pymysql
#定义数据库查询
class expect_sql:
    def __init__(self,sql):
        self.sql = sql

    def get_conn(self):
        conn = pymysql.connect(host= config.server,
                               port= config.port,
                               database= config.database,
                               user= config.userid,
                               password= config.pwd,
                               autocommit=True
                               )
        #创建游标对象
        cursor = conn.cursor()
        #发送sql
        cursor.execute(self.sql)
        row = cursor.fetchone()
        #释放资源
        cursor.close()
        conn.close()
        return row
