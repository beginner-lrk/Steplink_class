import unittest
import os
import app
import requests
from tools.SendRequest import RunMethod
import json
import paramunittest
import api.Log
log = api.Log.logger
from tools.ReadExcelCsv import ExcelCsv

path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
file_path = path + "/data/卡券测试用例.xls"
coupondata = ExcelCsv(file_path, "Sheet1").read_wxcel()
@paramunittest.parametrized(*coupondata)
class TestCoupon(unittest.TestCase):
    def setParameters(self,method,url,data,header,judge):
        self.header = json.loads(header)
        self.data = json.loads(data)
        self.url = app.BASE_URL + url
        self.method = method
        self.judge = int(judge)
    def setUp(self):
        print("开始执行测试用例")
    def tearDown(self):
        print("测试用例执行结束")
    def test01(self):
        print( self.method,self.url, self.header,self.data, self.judge)
        res= RunMethod().run_main(method=self.method,url=self.url,data=self.data,headers=self.header)
        print(res)
        print(res)
        self.assertEqual(res,self.judge)

if __name__ == "__main__":
    #实例化对象
    site = unittest.TestSuite()
    #调用测试方法
    site.addTest(unittest.makeSuite(TestCoupon))
    #执行测试套件
    runner = unittest.TextTestRunner()
    runner.run(site)
