#coding:utf-8

import sys
sys.path.append("..")

from apiconfig import *
import requests
import json

class chatroom:
    def __init__(self,headers,CteroomBody,modifyBody,MultiMemBody):
        self.headers = headers
        self.CteroomBody = CteroomBody
        self.modifyBody = modifyBody
        self.MultiMemBody = MultiMemBody

    def Ctechatroom(self):
        # Create Chatroom
        try:
            self.r = requests.post("%s/%s/%s/chatrooms" % (url, org, app),
                                   data=json.dumps(self.CteroomBody),
                                   headers=self.headers)
            data = self.r.json()
            if data['data']['id']:
                global RoomID
                RoomID = data['data']['id']
                print "Create chat room success, room id is: ", RoomID
                print json.dumps(data, sort_keys=True, indent=2)
                return True, RoomID
            else:
                print "Create chat room Failed"
                return False, None
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e, None

    @ornament
    def getAllRoom(self):
        # get all  Chatroom
        try:
            self.r = requests.get("%s/%s/%s/chatrooms" % (url, org, app),
                                   headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def ModifyRoom(self,roomid):
        # modify the  Chatroom
        try:
            self.r = requests.put("%s/%s/%s/chatrooms/%s" % (url, org, app,roomid),
                                  data=json.dumps(self.modifyBody),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def getRoomDetail(self, roomid):
        # get the  Chatroom details
        try:
            self.r = requests.get("%s/%s/%s/chatrooms/%s" % (url, org, app, roomid),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def InviteMemRoom(self, roomid,userroom):
        # Invite a member to  Chatroom
        try:
            self.r = requests.post("%s/%s/%s/chatrooms/%s/users/%s" % (url, org, app, roomid,userroom),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def InvMultiMemRoom(self, roomid):
        # Invite multi member to Chatroom
        try:
            self.r = requests.post("%s/%s/%s/chatrooms/%s/users" % (url, org, app, roomid),
                                  data=json.dumps(self.MultiMemBody),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def KickMemRoom(self, roomid, userroom):
        # Kick a member from Chatroom
        try:
            self.r = requests.delete("%s/%s/%s/chatrooms/%s/users/%s" % (url, org, app, roomid, userroom),
                                   headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def KickMultiMemRoom(self, roomid):
        # Kick multi member from Chatroom
        try:
            self.r = requests.delete("%s/%s/%s/chatrooms/%s/users/%s,%s" % (url, org, app, roomid,user3,user4),
                                   headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def getJoinAllRoom(self, roomuser):
        # get user joined all Chatroom
        try:
            self.r = requests.get("%s/%s/%s/users/%s/joined_chatrooms" % (url, org, app, roomuser),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def getAllRobot(self):
        # get all robots
        try:
            self.r = requests.get("%s/%s/%s/robots" % (url, org, app),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def SendMessRoom(self, roomid):
        # send messages to Chatroom
        sendMessRoom = {"target_type": "chatrooms",
                        "target": [roomid],
                        "msg": {
                            "type": "txt",
                            "msg": "this message is test chatroom from rest"
                        },
                        "from": "rest_auto"
                        }
        try:
            self.r = requests.post("%s/%s/%s/messages" % (url, org, app),
                                   data=json.dumps(sendMessRoom),
                                   headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def AddAdminRoom(self,roomid,roomuser):
        # add an chatroom admin
        AddAdminBody = {"newadmin": roomuser}
        try:
            self.r = requests.post("%s/%s/%s/chatrooms/%s/admin" % (url, org, app, roomid),
                                   data=json.dumps(AddAdminBody),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def getAdminList(self, roomid):
        # get an chatroom admin list
        try:
            self.r = requests.get("%s/%s/%s/chatrooms/%s/admin" % (url, org, app, roomid),
                                   headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def RmRoomAdmin(self, roomid, roomuser):
        # remove an chatroom admin
        try:
            self.r = requests.delete("%s/%s/%s/chatrooms/%s/admin/%s" % (url, org, app, roomid,roomuser),
                                   headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def MuteMember(self, roomid, roomuser):
        # mute a member
        MuteMemBody = {"usernames": [roomuser], "mute_duration": 86400000}
        try:
            self.r = requests.post("%s/%s/%s/chatrooms/%s/mute" % (url, org, app, roomid),
                                     data=json.dumps(MuteMemBody),
                                     headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def getMuteList(self, roomid):
        # get mute membet list
        try:
            self.r = requests.get("%s/%s/%s/chatrooms/%s/mute" % (url, org, app, roomid),
                                   headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def RmMuteMember(self, roomid,roomuser):
        # Remove a mute membet
        try:
            self.r = requests.delete("%s/%s/%s/chatrooms/%s/mute/%s" % (url, org, app, roomid, roomuser),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def DelChatRoom(self, roomid):
        # delete a chatroom
        try:
            self.r = requests.delete("%s/%s/%s/chatrooms/%s" % (url, org, app, roomid),
                                  headers=self.headers)
        except requests.exceptions.ConnectionError, e:
            return "Your url is error: " % e
        else:
            return self.r