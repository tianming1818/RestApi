#coding:utf-8

import sys
sys.path.append("..")

from apiconfig import *
import requests
import json

class GroupsInfo:
    def __init__(self,headers):
        self.headers = headers

    @ornament
    def getAllGroups(self):
        #get All Groups infomation
        try:
            self.r = requests.get("%s/%s/%s/chatgroups" %(url,org,app), headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def getLimitGroups(self):
        #get 10 Groups infomation
        try:
            self.r = requests.get("%s/%s/%s/chatgroups?limit=10" %(url,org,app), headers=self.headers)
            self.data = self.r.json()
            self.groupid = self.data['data'][0]['groupid']
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def getPublicGroups(self):
        #get All Public Groups infomation
        try:
            self.r = requests.get("%s/%s/%s/publicchatgroups" %(url,org,app), headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def getGroupDetail(self):
        #get  Groups infomation
        self.getLimitGroups()
        try:
            self.r = requests.get("%s/%s/%s/chatgroups/%s" %(url,org,app,self.groupid), headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r


