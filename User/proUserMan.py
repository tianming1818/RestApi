#coding:utf-8

import sys
sys.path.append("..")

from apiconfig import *
import requests
import json

class UserManage:
    def __init__(self,headers,userToken,cteUserBody,cteMultiUsrBody,setPWordBody,nicknameBody):
        self.headers = headers
        self.userToken = userToken
        self.cteUserBody = cteUserBody
        self.cteMultiUsrBody = cteMultiUsrBody
        self.setPWordBody = setPWordBody
        self.nicknameBody = nicknameBody

    def getClitSecret(self):
        # get client secret
        try:
            self.r = requests.get("%s/%s/%s/credentials" % (url, org, app),
                                  headers=self.headers)
            data = self.r.json()
            if data['credentials']['client_id']:
                client_id = data['credentials']['client_id']
                client_secret = data['credentials']['client_secret']
                print "Get client secret success, client_id is: %s, client_secret is: %s" %(client_id,client_secret)
                print json.dumps(data, sort_keys=True, indent=2)
                return True, client_id,client_secret
            else:
                print "Get client secret Failed"
                return False, None, None
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e, None, None

    @ornament
    def getAdminToken(self, client_id,client_secret):
        # get admin token
        admTokenBody = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret
        }
        try:
            self.r = requests.post("%s/%s/%s/token" % (url, org, app),
                                   data=json.dumps(admTokenBody),
                                   headers={'Content-Type': 'application/json'})
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def getUserToken(self):
        # get user token
        try:
            self.r = requests.post("%s/%s/%s/token" % (url, org, app),
                                   data=json.dumps(self.userToken),
                                   headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def getAllUser(self):
        # get All user info
        try:
            self.r = requests.get("%s/%s/%s/users" % (url, org, app),
                                   headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def CreateUser(self):
        # create a user
        try:
            self.r = requests.post("%s/%s/%s/users" % (url, org, app),
                                  data=json.dumps(self.cteUserBody),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def CrteMulieUser(self):
        # create multi users
        try:
            self.r = requests.post("%s/%s/%s/users" % (url, org, app),
                                   data=json.dumps(self.cteMultiUsrBody),
                                   headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def getUserDetail(self):
        # get a user details
        try:
            self.r = requests.get("%s/%s/%s/users/%s" % (url, org, app,user5),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def getMulUsrDetail(self):
        # get Multi user detail
        try:
            self.r = requests.get("%s/%s/%s/users?limit=30" % (url, org, app),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def ChkOnlineStat(self):
        # check user onine status
        try:
            self.r = requests.get("%s/%s/%s/users/%s/status" % (url, org, app, user1),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def deleteUser(self,user):
        # delete a user
        try:
            self.r = requests.delete("%s/%s/%s/users/%s" % (url, org, app, user),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def delMultiUser(self):
        # delete multi users
        try:
            self.r = requests.delete("%s/%s/%s/users?limit=5" % (url, org, app),
                                     headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def ResetPword(self):
        # reset password to user
        try:
            self.r = requests.put("%s/%s/%s/users/%s/password" % (url, org, app, user5),
                                  data=json.dumps(self.setPWordBody),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def ModifyNickname(self):
        # modify nickname for user
        try:
            self.r = requests.put("%s/%s/%s/users/%s" % (url, org, app, user5),
                                  data=json.dumps(self.nicknameBody),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def addFriends(self,user,friend):
        # add friend for user
        try:
            self.r = requests.post("%s/%s/%s/users/%s/contacts/users/%s" % (url, org, app, user,friend),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def delFriends(self, user, friend):
        # del friend for user
        try:
            self.r = requests.delete("%s/%s/%s/users/%s/contacts/users/%s" % (url, org, app, user, friend),
                                   headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def FriendsList(self, user):
        # get friend list
        try:
            self.r = requests.get("%s/%s/%s/users/%s/contacts/users" % (url, org, app, user),
                                     headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def MvToBlack(self, user,friend):
        # move friend to black list
        MvblackBody = {"usernames": [friend]}
        try:
            self.r = requests.post("%s/%s/%s/users/%s/blocks/users" % (url, org, app, user),
                                   data=json.dumps(MvblackBody),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def GetBlackList(self, user):
        # get user  black list
        try:
            self.r = requests.get("%s/%s/%s/users/%s/blocks/users" % (url, org, app, user),
                                   headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def RmBlkList(self, user,blackuser):
        # remove friend from black list
        try:
            self.r = requests.delete("%s/%s/%s/users/%s/blocks/users/%s" % (url, org, app, user,blackuser),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def DeactivateUser(self, user):
        # Deactivate a User
        try:
            self.r = requests.post("%s/%s/%s/users/%s/deactivate" % (url, org, app, user),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def ActivateUser(self, user):
        # Activate a User
        try:
            self.r = requests.post("%s/%s/%s/users/%s/activate" % (url, org, app, user),
                                   headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def DisconnectUser(self):
        # Disconnect User
        try:
            self.r = requests.get("%s/%s/%s/users/%s/disconnect" % (url, org, app, user1),
                                   headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

