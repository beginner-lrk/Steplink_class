#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/3/16 19:14
import os
import logging
from logging.handlers import TimedRotatingFileHandler
import time
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
log_path = os.path.join(path,'log')
class Logger:
    #
    def __init__(self,logger_name='logs...'):   #定义写日志的对象，默认叫做logs...
        self.logger = logging.getLogger(logger_name)
        #self.logger.setLevel(level=logging.INFO)
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name = 'logs'   #日志文件名
        self.backup_count = 5    #最多存放日志的数量
        #日志输出级别
        self.console_output_level = 'WARNING'
        self.file_output_level = 'INFO'
        #日志输出格式
        self.formatter = logging.Formatter("%(asctime)s -%(filename)s[%(lineno)d]-%(levelname)s -%(message)s ")

    def get_logger(self):
        #多次调用出现重复打印，在获取logger对象的时候判断是否已有handlers
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            #每天重新创建一个日志文件
            file_handler = TimedRotatingFileHandler(filename=os.path.join(log_path,self.log_file_name),when='D',
                                                    interval=1,backupCount=self.backup_count,delay=True,
                                                    encoding='utf-8')
            file_handler.setFormatter(self.formatter) #设置日志格式
            file_handler.setLevel(self.file_output_level) #输出到文件日志等级
            self.logger.addHandler(file_handler)  #将日志输出到日志文件
        return self.logger

logger = Logger().get_logger()


