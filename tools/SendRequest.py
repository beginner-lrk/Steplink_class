#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/3/11 10:42
import requests
import json
import app

class RunMethod(object):

    def request_get(self, url, data=None, headers=None):
        # 发起一次GET请求时，参数会以url string的形式进行传递。(Query String Parameters)即?后的字符串则为其请求参数，并以&作为分隔符。
        data = json.dumps(data)
        if headers != None:
            response = requests.get(url=url, data=data, headers= headers).json()
        else:
            response = requests.get(url=url, data=data).json()
        #用dumps将python编码成json字符串
        response = json.dumps(response, ensure_ascii=False, sort_keys=True)
        #print("response",res)
        response = json.loads(response)
        res = response["code"]
        #print(res)
        print("get请求")
        return res

    def request_post(self, url, data, headers=None):
        data = json.dumps(data)
        if headers != None:
            response = requests.post(url=url, data=data, headers= headers).json()
        else:
            response = requests.post(url=url, data=data).json()
        #用dumps将python编码成json字符串
        response = json.dumps(response,ensure_ascii=False,sort_keys =True)
        #print("response",res)
        response = json.loads(response)
        res = response["code"]
        #print(res)
        print("post请求")
        return res

    def run_main(self, method, url, data, headers):
        if method == "get":
            response = self.request_get(url, data, headers)
        else:
            response = self.request_post(url, data, headers)
        return response
if __name__ == '__main__':  # 通过写死参数，来验证我们写的请求是否正确
    myheader = app.header
    mydata = {"type":2,"name":"抵用测试B","maxPublishNum":"20","useTimeType":1,"startTime":"","endTime":"","validDays":"3","minUsePriceYuan":0,"discountPriceYuan":"1","discountNumStr":0,"maxDiscountPriceYuan":"","useScene":1,"cover":"","isSuperposition":0,"maxSuperpositionNum":0,"publishStartTime":"2021-03-28 00:00:00","publishEndTime":"2021-03-31 00:00:00","customerType":2,"customerCouponNum":-1,"goodsType":"0","goodsIds":[],"goodsList":[],"remark":"测试","createTime":""}
    res= RunMethod().run_main(method='get', url='https://crmhd.linker.cc/crm/pc/coupon/getlist?type=0&pageIndex=1&pageSize=20', data=None,headers= app.header)
    res1 = RunMethod().run_main(method='post',
                               url='https://crmhd.linker.cc/crm/pc/coupon/add',
                               data=mydata, headers=app.header)
    print(res)
    print(res1)