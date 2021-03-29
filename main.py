# 因为config下面加上了__int__.py文件可以直接导包
# from config import config
#导包
import unittest
import app
import tools.HTMLTestRunner as HTMLTestRunner
import time
import api.Log
log = api.Log.logger

def all_cases():
    rule = "TestCoupon.py"
    pa = app.BASE_DIR + "/testcase"
    discover = unittest.defaultTestLoader.discover(start_dir=pa,pattern=rule,top_level_dir=None)
    print(discover)
    log.info(discover)
    return discover
if __name__ == '__main__':
    report_dir = app.BASE_DIR + '/report/report{}.html'.format(time.strftime("%Y%m%d%H%M%S"))
    log.info(report_dir)
    fp = open(report_dir,"wb")
    runCaseReport = HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2, title="卡券接口测试报告", description="添加删除编辑接口")
    runCaseReport.run(all_cases())
    fp.close()


   # smtp = SMTP(user="liurike4295@qq.com", password="199406160818ke", host="smtp.qq.com")
   # smtp.sender(to="liu_rike@hzlh.com", attachments=file)