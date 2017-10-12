#coding:utf-8

import sys
sys.path.append("..")

from apiconfig import *
import requests
import json

#setup body parameters
sendbody = {"target_type": "users",
                     "target": [user1],
                     "msg": {
                         "type": "txt",
                         "msg": messages
                     },
                     "from": "rest"
                     }

sendbodytwo={ "target_type":"users",
                 "target":[user1,user2],
                 "msg":{
                 "type":"txt",
                 "msg": messages
                  },
                  "from":"rest"
                }

sendImagebody = { "target_type":"users",
    "target":[user1,user2],
    "msg":{
        "type":"img",
        "url":"https://a1.easemob.com/easemob-demo/chatdemoui/chatfiles/c8ae5ad0-a5a7-11e6-b991-65e029430485",
        "filename":"lorex.jpg",
        "secret":"yK5a2qWnEeaRcJUaVNstNOVVTjuqBVyib-rF7Vw1xSVn28X4",
        "size":{
        "width":480,
        "height":480
      }
     },
    "from":"rest"
}

sendAudiobody = { "target_type":"users",
    "target":[user1,user2],
    "msg":{
        "type":"audio",
        "url":"https://a1.easemob.com/easemob-demo/chatdemoui/chatfiles/76635950-a5a8-11e6-9387-3f2d3a91e533",
        "filename":"audio sample.amr",
        "secret":"dmNZWqWoEeaDymsQPaQ9I3Wcs05uXfMWGn0KuRdR87wqko70",
        "size":{
        "width":480,
        "height":480
      }
     },
    "from":"rest"
}

sendVideobody = { "target_type":"users",
    "target":[user1,user2],
    "msg":{
        "type":"video",
        "url":"https://a1.easemob.com/easemob-demo/chatdemoui/chatfiles/9887d140-a649-11e6-b383-4541f7075ce8",
        "filename":"111.mp4",
        "length": 5,
        "secret":"mIfRSqZJEeaei5tHtLW4f-e_Zh4N_-DOwtX4nFIOvUitGtHJ",
        "thumb": "https://a1.easemob.com/easemob-demo/chatdemoui/chatfiles/f6a5a3a0-a64a-11e6-8a7b-51138be95708",
        "thumb_secret": "9qWjqqZKEeaeHwuBpYinrXmDsuAtOTQ2Ad8JW34Gtdj5XrnD",
        "file_length": 8699
     },
    "from":"rest"
}

sendNoticebody = {
    "target_type": "users",
    "target": [
        user2
    ],
    "msg": {
        "type": "txt",
        "msg": "公告标题"
    },
    "ext": {
      "info":[ {
            "txt": "测试文字a's'da'd'as'd'as'd"
        },
        {
            "img": "http://img002.21cnimg.com/photos/album/20160326/m600/B920004B5414AE4C7D6F2BAB2966491E.jpeg"
        },
        {
            "txt": "测试文字a's'da'd'as'd'as'd"
        }, {
            "img": "http://img002.21cnimg.com/photos/album/20160326/m600/B920004B5414AE4C7D6F2BAB2966491E.jpeg"
        },
        {
            "img": "http://img001.21cnimg.com/photos/album/20170220/m600/E6BA09D87E03DB8E06E5B1B8EC6958DC.gif"
        }]
    }
}

sendLocbody = { "target_type":"users",
    "target":[user2],
    "msg":{
      "addr":"中国北京市海淀区南大街2号院-1",
      "lat":"39.966334",
      "lng":"116.323123",
      "type":"loc"
    },
    "from":"rest"
}

sendForceNotibody = {"target_type" : "users",
 "target" : [user2],
 "msg" : {"type" : "txt","msg" : "hello from rest"},
 "from" : "admin",
 "ext" : {"em_force_notification":"true"} }

sendPushTitlebody = {"target_type":"users",
 "target":[user2],
 "msg" :
 {"type":"txt","msg":"hello"},
 "from":"test2",
"ext":{"em_apns_ext":{"em_push_title":"北京市海淀区中关村南大街2号数码大厦A座20层环信即时通讯云"}
}
}

PushNewTitlebody = {"target_type" : "users",
 "target": [user1],
 "msg":
 {"type":"txt","msg" : "this rest message for new push title"},
 "from":"rest",
"ext":{"em_apns_ext":{"em_push_name":"北京市海淀区","em_push_content":"this is content","extern":"11111"} }
}

sendIgnoreNotibody = {
    "target_type":"users",
    "target":[
      user1
    ],
    "msg":{
      "type":"txt",
      "msg":"hello from rest"
    },
    "from":"rest",
    "ext":{
      "em_ignore_notification":"true"
    }
  }

sendPushBadgebody = {"target_type" : "users",
 "target" : [user1],
 "msg" :
 {"type" : "txt",
 "msg" : "hello"},
 "from" : "rest",
"ext" : {"em_apns_ext" :{"em_push_badge":"37"}
}
}

sendPushIgnSoundbody = {"target_type" : "users",
 "target" : [user1],
 "msg" :
 {"type" : "txt",
 "msg" : "hello"},
 "from" : "rest",
"ext" : {"em_apns_ext" :{"em_push_ignore_sound":"false"}}
}

class TextMessage:
    def __init__(self, headers, body, bodytwo,sendImagebody,sendAudiobody,sendVideobody,sendNoticebody,sendLocbody,
                 sendForceNotibody,sendPushTitlebody,sendIgnoreNotibody,sendPushBadgebody,sendPushIgnSoundbody,
                 PushNewTitlebody):
        self.headers = headers
        self.body = body
        self.bodytwo = bodytwo
        self.sendImagebody = sendImagebody
        self.sendAudiobody = sendAudiobody
        self.sendVideobody = sendVideobody
        self.sendNoticebody = sendNoticebody
        self.sendLocbody = sendLocbody
        self.sendForceNotibody = sendForceNotibody
        self.sendPushTitlebody = sendPushTitlebody
        self.sendIgnoreNotibody = sendIgnoreNotibody
        self.sendPushBadgebody = sendPushBadgebody
        self.sendPushIgnSoundbody = sendPushIgnSoundbody
        self.PushNewTitlebody = PushNewTitlebody

    @ornament
    def sendmessage(self):
        #send a messages to one user
        try:
            self.r = requests.post("%s/%s/%s/messages" %(url,org,app), data=json.dumps(self.body), headers=self.headers)
            #print r.json()
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def send_two(self):
        # send a messages to one user
        try:
            self.r = requests.post("%s/%s/%s/messages" %(url,org,app), data=json.dumps(self.bodytwo), headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def get_friend(self):
        # get a user the friends list
        try:
            self.r = requests.get("%s/%s/%s/users/%s/contacts/users" %(url,org,app,user1), headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def sendImageMess(self):
        # send a Image messages to user
        try:
            self.r = requests.post("%s/%s/%s/messages" %(url,org,app), data=json.dumps(self.sendImagebody), headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def sendAudioMess(self):
        # send a audio messages to  user
        try:
            self.r = requests.post("%s/%s/%s/messages" %(url,org,app), data=json.dumps(self.sendAudiobody), headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def sendVideoMess(self):
        try:
            self.r = requests.post("%s/%s/%s/messages" %(url,org,app), data=json.dumps(self.sendVideobody), headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def sendNoticeMess(self):
        try:
            self.r = requests.post("%s/%s/%s/messages" %(url,org,app), data=json.dumps(self.sendNoticebody), headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def sendLocMess(self):
        try:
            self.r = requests.post("%s/%s/%s/messages" %(url,org,app), data=json.dumps(self.sendLocbody), headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def sendForceNotiMess(self):
        try:
            self.r = requests.post("%s/%s/%s/messages" %(url,org,app), data=json.dumps(self.sendForceNotibody), headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def sendPushTitleMess(self):
        try:
            self.r = requests.post("%s/%s/%s/messages" %(url,org,app), data=json.dumps(self.sendPushTitlebody), headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def sendIgnoreNotiMess(self):
        try:
            self.r = requests.post("%s/%s/%s/messages" %(url,org,app), data=json.dumps(self.sendIgnoreNotibody), headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def sendPushBadgeMess(self):
        try:
            self.r = requests.post("%s/%s/%s/messages" %(url,org,app), data=json.dumps(self.sendPushBadgebody), headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def sendPushIgSoundMess(self):
        try:
            self.r = requests.post("%s/%s/%s/messages" %(url,org,app), data=json.dumps(self.sendPushIgnSoundbody), headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

    @ornament
    def PushNewTitleMess(self):
        try:
            self.r = requests.post("%s/%s/%s/messages" %(url,org,app), data=json.dumps(self.PushNewTitlebody), headers=self.headers)
        except requests.exceptions.ConnectionError,e:
            return "Your url is error: " % e
        else:
            return self.r

'''
Upload Image File
Upload Audio File
Upload Video File
'''