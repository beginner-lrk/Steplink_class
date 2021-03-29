#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/3/10 13:50
import unittest
from parameterized import parameterized
from api.CouponAdd import CouponAdd
import csv
import codecs
from itertools import islice
import os
from tools.expectsql import expect_sql
import api.Log
log = api.Log.logger

#当使用main主文件执行时必须重新获取路径
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
pathcsv = path + "/data/coupondata.csv"
#读取本地CSV文件
data = csv.reader(codecs.open(pathcsv,'r','gbk',"ignore"))
#存放用户数据
coupondata = []

#循环获取每行信息
for line in islice(data,1,None):
    coupondata.append(line)
print(coupondata)

log.info(coupondata)

class TestCoupon(unittest.TestCase):
    #数据动态导入参数化

    def setUp(self):
        print("测试卡券新增接口")
    def tearDown(self):
        print("卡券接口测试结束")
    @parameterized.expand(coupondata)
    def test01(self,name,type,maxPublishNum,publishStartTime):
        try:
            print(name)
            response = CouponAdd()
            res = response.coupon_add(name,type,maxPublishNum,publishStartTime)
            #返回响应码
            #res_po = res.status_code
            print(res.text)
            sql ='SELECT create_customer_id from t_coupon where name = "大麦测试A";'
            expect_value = expect_sql(sql).get_conn()
            expect = expect_value[0]
            #打印超时时间
            #print(res.elapsed.total_seconds())
            #断言请求成功
            #self.assertEqual(res_po, 200)
            #断言数据熙增成功
            self.assertIn('10049',expect)
        except Exception as e:
            print(e)



if __name__ == "__main__":
    #实例化对象
    site = unittest.TestSuite()
    #调用测试方法
    site.addTest(unittest.makeSuite(TestCoupon))
    #执行测试套件
    runner = unittest.TextTestRunner()
    runner.run(site)
