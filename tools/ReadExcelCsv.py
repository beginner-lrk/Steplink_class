#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/3/25 18:58
import csv
from itertools import islice
import os
import xlrd

class ExcelCsv:
    def __init__(self,file_path,sheet_name):
        self.file_path = file_path
        self.sheet_name = sheet_name
    def read_csv(self):
        #该方法返回的是只是参数值
        try:
            with open(self.file_path,'r',encoding='gbk') as f:
                reader = csv.reader(f)
                csvlist = []
                for line in islice(reader, 1, None):
                        csvlist.append(line)
                return csvlist
        except FileNotFoundError:
            return ('未找到测试文件')
    def read_wxcel(self):
        # 该方法返回的是用例
        data = xlrd.open_workbook(self.file_path) #打开excel文件
        table = data.sheet_by_name(self.sheet_name) #通过名称获取sheel表单
        data.sheet_loaded(self.sheet_name)   #检查sheet是否导入完毕
        datalist = []
        nrows = table.nrows #获取行数
        data_value = table.row_values(0) #获取第一行的标题
        print(data_value)
        for i in range(1,nrows):
            if table.row_values(i)[0] != u'case_id':  # 如果这个Excel的这个sheet的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]
                datalist.append(table.row_values(i,start_colx=2, end_colx=7))
        return datalist


if __name__ == "__main__":
    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    file_path =  path + "/data/卡券测试用例.xls"
    csv = ExcelCsv(file_path,"Sheet1").read_wxcel()
    print(csv)
