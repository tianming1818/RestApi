#coding:utf-8

import sys
sys.path.append("..")

from apiconfig import *
import requests
import json

##setup callback parameters
CBName = "mycallback"

addbody = {"name":CBName,
    "msgTypes":["chat","chat_offline"],
    "hxSecret":"123456",
    "secret":"654321",
    "targetUrl":"http://121.41.60.67:8082/callback/",
    "status":1,
    "notifyUrl":"http://www.notify.com"}

modifybody = {"name":"mycallback",
    "msgTypes":["chat","chat_offline"],
    "hxSecret":"123456",
    "secret":"654321",
    "targetUrl":"http://121.41.60.67:8082/callback/",
    "status":1,
    "notifyUrl":"http://www.notify.com"}


class HxCallback:
    def __init__(self, headers, addbody,modifybody):
        self.headers = headers
        self.body = addbody
        self.modifybody = modifybody

    @ornament
    def addcallback(self):
        try:
            self.r = requests.post("%s/%s/%s/callbacks" %(url,org,app), data=json.dumps(self.body), headers=self.headers)
            #print r.json()
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def querycallbacks(self):
        try:
            self.r = requests.get("%s/%s/%s/callbacks" %(url,org,app),headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def queryCBDetail(self):
        try:
            self.r = requests.get("%s/%s/%s/callbacks/%s" %(url,org,app,CBName),headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def modifyCB(self):
        try:
            self.r = requests.put("%s/%s/%s/callbacks/%s" %(url,org,app,CBName),data=json.dumps(self.modifybody),headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def deleteCB(self):
        try:
            self.r = requests.delete("%s/%s/%s/callbacks/%s" %(url,org,app,CBName),data=json.dumps(self.modifybody),headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r