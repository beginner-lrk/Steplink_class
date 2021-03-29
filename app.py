#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/3/5 19:42
#封装程序常量
import os
#默认URL
LoginUrl = ""
BASE_URL = "https://crmhd.linker.cc/crm"
header = {"Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "PCHT": "8618925123b79d16dd04661eda08bfdc",
            "Content-Type":"application/json;charset=UTF-8"
            }
PCHT = "f2ec6b967cbb8eb4794a9ced4db65726"
#项目路径
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

#用户TOKEN
TOKEN = None