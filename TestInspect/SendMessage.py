#coding= utf-8
import sys
import unittest


sys.path.append("..")

from apiconfig import *
from Chat.sendmessages import *


class TestMessageTestCase(unittest.TestCase):
    def setUp(self):
        self.STM = TextMessage(headers,sendbody,sendbodytwo,sendImagebody,sendAudiobody,sendVideobody,
                               sendNoticebody,sendLocbody,sendForceNotibody,sendPushTitlebody,sendIgnoreNotibody,
                               sendPushBadgebody,sendPushIgnSoundbody,PushNewTitlebody)

    def testTM(self):
        u'''发送一个人消息'''
        self.assertEqual(self.STM.sendmessage(), 200)

    def testSendtwo(self):
        u'''发送两个人消息'''
        self.assertEqual(self.STM.send_two(),200)

    def getfriend(self):
        u'''获取好友名单'''
        self.assertEqual(self.STM.get_friend(),200)

    def testsendImage(self):
        u'''发送图片消息'''
        self.assertEqual(self.STM.sendImageMess(),200)

    def testsendAudio(self):
        u'''发送声音消息'''
        self.assertEqual(self.STM.sendAudioMess(),200)

    def testsendVideo(self):
        u'''发送视频消息'''
        self.assertEqual(self.STM.sendVideoMess(),200)

    def testsendNotic(self):
        u'''发送公告消息'''
        self.assertEqual(self.STM.sendNoticeMess(),200)

    def testsendLoc(self):
        u'''发送位置消息'''
        self.assertEqual(self.STM.sendLocMess(),200)

    def testForceNotifi(self):
        u'''发送强制通知'''
        self.assertEqual(self.STM.sendForceNotiMess(),200)

    def testPushTitle(self):
        u'''测试推送title'''
        self.assertEqual(self.STM.sendPushTitleMess(),200)

    def testIgnoreNotifi(self):
        u'''发送忽略通知'''
        self.assertEqual(self.STM.sendIgnoreNotiMess(),200)

    def testPushBadge(self):
        u'''推送标记'''
        self.assertEqual(self.STM.sendPushBadgeMess(),200)

    def testPushIgSound(self):
        u'''推送忽略声音'''
        self.assertEqual(self.STM.sendPushIgSoundMess(),200)

    def testPushNewTitle(self):
        u'''测试推送新的title格式'''
        self.assertEqual(self.STM.PushNewTitleMess(),200)


    def tearDown(self):
        self.STM = None