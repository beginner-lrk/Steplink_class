#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/3/5 19:36
import app
import requests

class CouponAdd:
    # 提交的json数据
    def __init__(self):
        self.myheader= app.header
        self.CouponAdd_url = app.BASE_URL + "/pc/coupon/add"
    def coupon_add(self,name,type,maxPublishNum,publishStartTime):
        myjson = {}
        if name :
            myjson["name"] = name
        if type:
            myjson["type"] = type
        if maxPublishNum:
            myjson["maxPublishNum"] = maxPublishNum
        if publishStartTime:
            myjson["publishStartTime"] = publishStartTime
        myjson = {"type":myjson["type"] ,
                  "name": myjson["name"],
                  "maxPublishNum": myjson["maxPublishNum"],
                  "useTimeType": 1,
                  "startTime": "",
                  "endTime": "",
                  "validDays": "3",
                  "minUsePriceYuan": 0,
                  "discountPriceYuan": "",
                  "discountNumStr": 0,
                  "maxDiscountPriceYuan": "",
                  "useScene": 1,
                  "cover": "",
                  "isSuperposition": 0,
                  "maxSuperpositionNum": 0,
                  "publishStartTime": myjson["publishStartTime"],
                  "publishEndTime": "2021-03-16 00:00:00",
                  "customerType": 0,
                  "customerCouponNum": -1,
                  "goodsType": "0",
                  "goodsIds": [],
                  "goodsList": [],
                  "remark": "haha",
                  "createTime": ""
                  }
        #超时时间不超过5s
        return requests.post(self.CouponAdd_url, json=myjson, headers=self.myheader,timeout=5)

