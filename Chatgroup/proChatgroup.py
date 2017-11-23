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
            global groupid,data
            data = self.r.json()
            groupid = data['data'][0]['groupid']
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
        print "groupid is: ",groupid
        try:
            self.r = requests.get("%s/%s/%s/chatgroups/%s" %(url,org,app,groupid), headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r
    @ornament
    def getMultiGrpDetail(self):
        #get multi Groups infomation
        groupid1 = data['data'][1]['groupid']
        groupid2 = data['data'][2]['groupid']
        groupid3 = data['data'][3]['groupid']
        print "multi groupid is: ",groupid1,groupid2,groupid3
        try:
            self.r = requests.get("%s/%s/%s/chatgroups/%s,%s,%s" %(url,org,app,groupid1,groupid2,groupid3), headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r
    @ornament
    def getGroupMember(self):
        #get Groups member
        print "groupid is: ",groupid
        try:
            self.r = requests.get("%s/%s/%s/chatgroups/%s/users" %(url,org,app,groupid), headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r
    @ornament
    def getGrpBlacklit(self):
        # get Groups black list
        print "groupid is: ", groupid
        try:
            self.r = requests.get("%s/%s/%s/chatgroups/%s/blocks/users" % (url, org, app, groupid), headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def getjoinAllGrp(self):
        # get user joined all Groups
        try:
            self.r = requests.get("%s/%s/%s/users/%s/joined_chatgroups" %(url, org, app, user1),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def getmutelist(self):
        # get group muted list
        print "groupid is: ", groupid
        try:
            self.r = requests.get("%s/%s/%s/chatgroups/%s/mute" % (url, org, app, groupid),headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def ShareFilelist(self):
        # get group share files list
        print "groupid is: ", groupid
        try:
            self.r = requests.get("%s/%s/%s/chatgroups/%s/share_files" % (url, org, app, groupid), headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def getAdminlist(self):
        # get group admin list
        print "groupid is: ", groupid
        try:
            self.r = requests.get("%s/%s/%s/chatgroups/%s/admin" % (url, org, app, groupid), headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r




class OperateGroup:
    def __init__(self,headers,CrePubGrpBody,multiMemBody,grpTransBody,modgrpBody,mulMemtoblackBody,
                 muteMemBody,addAdminBody,pubGrpVerifyBody,verifyBody,privateBody,privateAllowBody):
        self.headers = headers
        self.cpgbody = CrePubGrpBody
        self.multiMem = multiMemBody
        self.transbody = grpTransBody
        self.modifygrp = modgrpBody
        self.MemstoblkBody = mulMemtoblackBody
        self.muteMemBody = muteMemBody
        self.addAdminBody = addAdminBody
        self.CPGVbody = pubGrpVerifyBody
        self.verifyBody = verifyBody
        self.privateBody = privateBody
        self.privateAllowBody = privateAllowBody

    def CrePubGrp(self):
        try:
            self.r = requests.post("%s/%s/%s/chatgroups" % (url, org, app),data=json.dumps(self.cpgbody), headers=self.headers)
            data = self.r.json()
            if data['data']['groupid']:
                global crePubGrpID
                crePubGrpID = data['data']['groupid']
                print "Create public groups success, group id is: ",crePubGrpID
                print json.dumps(data, sort_keys=True, indent=2)
                return True,crePubGrpID
            else:
                print "Create public groups Failed"
                return False,None
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e,None
        else:
            return self.r,None

    @ornament
    def groupAddMem(self,groupid):
        # add a membet go group
        print "groupid is: ", groupid
        try:
            self.r = requests.post("%s/%s/%s/chatgroups/%s/users/%s" % (url, org, app, groupid,user3), headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def GrpAddMulMem(self, groupid):
        # add multi membet go group
        print "groupid is: ", groupid
        try:
            self.r = requests.post("%s/%s/%s/chatgroups/%s/users/" % (url, org, app, groupid),data=json.dumps(self.multiMem),
                                   headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def GrpTransfer(self, groupid):
        # group Transfer
        print "groupid is: ", groupid
        try:
            self.r = requests.put("%s/%s/%s/chatgroups/%s" % (url, org, app, groupid),
                                   data=json.dumps(self.transbody),
                                   headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def modifyGrp(self, groupid):
        # modify group
        print "groupid is: ", groupid
        try:
            self.r = requests.put("%s/%s/%s/chatgroups/%s" % (url, org, app, groupid),
                                  data=json.dumps(self.modifygrp),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def delGrpMem(self, groupid):
        # delete a group membet
        print "groupid is: ", groupid
        try:
            self.r = requests.delete("%s/%s/%s/chatgroups/%s/users/%s" % (url, org, app, groupid, user3),
                                   headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def delMultiMem(self, groupid):
        # delete multi group membet
        print "groupid is: ", groupid
        try:
            self.r = requests.delete("%s/%s/%s/chatgroups/%s/users/%s,%s" % (url, org, app, groupid, user4,user5),
                                     headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def MemToBlack(self, groupid):
        #move group member to black
        print "groupid is: ", groupid
        try:
            self.r = requests.post("%s/%s/%s/chatgroups/%s/blocks/users/%s" % (url, org, app, groupid, user3),
                                     headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def MultiMemToBlack(self, groupid):
        # move multi group member to black
        print "groupid is: ", groupid
        try:
            self.r = requests.post("%s/%s/%s/chatgroups/%s/blocks/users" % (url, org, app, groupid),
                                   data=json.dumps(self.MemstoblkBody),
                                   headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def RmBlackMem(self, groupid):
        #rm member from black
        print "groupid is: ", groupid
        try:
            self.r = requests.delete("%s/%s/%s/chatgroups/%s/blocks/users/%s" % (url, org, app, groupid, user3),
                                     headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def RmBlkMultiMem(self, groupid):
        # rm multi member from black
        print "groupid is: ", groupid
        try:
            self.r = requests.delete("%s/%s/%s/chatgroups/%s/blocks/users/%s,%s" % (url, org, app, groupid, user4,user5),
                                     headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def sendGrpMess(self, groupid):
        # send group message
        sendmessBody = { "target_type":"chatgroups",
                 "target":[groupid],
                 "msg":{
                 "type":"txt",
                 "msg":messages
                },
                "from":"rest"
        }
        print "groupid is: ", groupid
        try:
            self.r = requests.post("%s/%s/%s/messages" %(url, org, app),data=json.dumps(sendmessBody),
                headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def MuteMember(self, groupid):
        # mute member
        print "groupid is: ", groupid
        try:
            self.r = requests.post(
                "%s/%s/%s/chatgroups/%s/mute" % (url, org, app, groupid),
                data = json.dumps(self.muteMemBody),
                headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def unMuteMember(self, groupid):
        # unmute member
        print "groupid is: ", groupid
        try:
            self.r = requests.delete(
                "%s/%s/%s/chatgroups/%s/mute/%s" % (url, org, app, groupid,user3),
                headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def addAdmin(self, groupid):
        # add a  member to admin
        print "groupid is: ", groupid
        try:
            self.r = requests.post(
                "%s/%s/%s/chatgroups/%s/admin" % (url, org, app, groupid),
                data=json.dumps(self.addAdminBody),
                headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def delAdmin(self, groupid):
        # delete a member to admin
        print "groupid is: ", groupid
        try:
            self.r = requests.delete(
                "%s/%s/%s/chatgroups/%s/admin/%s" % (url, org, app, groupid,user1),
                headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def ApplyJoinGrp(self, groupid):
        # apply to join group
        print "groupid is: ", groupid
        try:
            tkBody =  {
                    "grant_type": "password",
                    "username": user3,
                    "password": "1"
                    }
            req = requests.post("%s/%s/%s/token" % (url, org, app), data=json.dumps(tkBody),
                                headers={'Accept': 'application/json', 'Content-Type': 'application/json'})
            if req.status_code == 200:
                contents = json.loads(req.content)
                usertokens = contents["access_token"]
                expires_in = contents["expires_in"]
                print "token is: ",usertokens
                print "expires is: ", expires_in
            else:
                print "get user token api error"
                print "status code is: ",req.status_code, req.content
            global userheaders
            userheaders = {'Accept': 'application/json',
                       'Content-Type': 'application/json',
                       'Authorization': "Bearer %s" % usertokens}
            self.r = requests.post(
                "%s/%s/%s/chatgroups/%s/apply" % (url, org, app, groupid),
                headers=userheaders)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def deleteGroup(self,groupid):
        # delete a group
        print "groupid is: ", groupid
        try:
            self.r = requests.delete("%s/%s/%s/chatgroups/%s" % (url, org, app, groupid), headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r


    def CrePubVerify(self):
        try:
            self.r = requests.post("%s/%s/%s/chatgroups" % (url, org, app),data=json.dumps(self.CPGVbody), headers=self.headers)
            data = self.r.json()
            if data['data']['groupid']:
                global cPubVrfyGrpID
                cPubVrfyGrpID = data['data']['groupid']
                print "Create public need verify groups success, group id is: ",cPubVrfyGrpID
                print json.dumps(data, sort_keys=True, indent=2)
                return True,cPubVrfyGrpID
            else:
                print "Create public need verify groups Failed"
                return False,None
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e,None
        else:
            return self.r,None

    @ornament
    def vefyAlyJoinGrp(self, groupid):
        # verify apply join group
        print "groupid is: ", groupid
        try:
            self.r = requests.post("%s/%s/%s/chatgroups/%s/apply_verify" % (url, org, app, groupid),
                                   data=json.dumps(self.verifyBody),
                                   headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    def CrePrivateGrp(self):
        try:
            self.r = requests.post("%s/%s/%s/chatgroups" % (url, org, app),data=json.dumps(self.privateBody), headers=self.headers)
            data = self.r.json()
            if data['data']['groupid']:
                global GroupID
                GroupID = data['data']['groupid']
                print "Create private groups success, group id is: ",GroupID
                print json.dumps(data, sort_keys=True, indent=2)
                return True,GroupID
            else:
                print "Create private groups Failed"
                return False,None
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e,None
        else:
            return self.r,None

    def CtePrivAllowGrp(self):
        try:
            self.r = requests.post("%s/%s/%s/chatgroups" % (url, org, app),data=json.dumps(self.privateAllowBody), headers=self.headers)
            data = self.r.json()
            if data['data']['groupid']:
                global GroupID
                GroupID = data['data']['groupid']
                print "Create private allow Invite groups success, group id is: ",GroupID
                print json.dumps(data, sort_keys=True, indent=2)
                return True,GroupID
            else:
                print "Create private allow Invite groups Failed"
                return False,None
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e,None
        else:
            return self.r,Nonev

    @ornament
    def LeaveGroup(self, groupid):
        # leave the group
        print "groupid is: ", groupid
        try:
            self.r = requests.delete("%s/%s/%s/chatgroups/%s/quit" % (url, org, app, groupid), headers=userheaders)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r





