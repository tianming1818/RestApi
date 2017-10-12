#coding= utf-8
import sys
import unittest


sys.path.append("..")

from apiconfig import *
from Chat.sendCMDgetInfo import *

class TestCmdMessageGetInfo(unittest.TestCase):

    def setUp(self):
        self.SCMGI = SendCmdGetInfo(headers,sendCmdbody,sendCmdStartDebugbody,sendCmdStopDebugbody,
                                    sendCmdUploadLogbody,sendCmdChagServerbody,sendCmdChagAppkeyboey,sendBroadcastbody)
    def testCmdMess(self):
        u'''发送一个命令消息'''
        self.assertEqual(self.SCMGI.sendCmdMess(), 200)

    def testCmdStartDebug(self):
        u'''发送命令开启debug'''
        self.assertEqual(self.SCMGI.sendCmdStartDebugmess(),200)

    def testCmdStopDebug(self):
        u'''发送命令关闭debug'''
        self.assertEqual(self.SCMGI.sendCmdStopDebugmess(),200)

    def testCmdUploadLog(self):
        u'''发送命令上传日志'''
        self.assertEqual(self.SCMGI.sendCmdUploadLogMess(),200)

    def testCmdChagServer(self):
        u'''发送命令改变服务器地址'''
        self.assertEqual(self.SCMGI.sendCmdChagServerMess(),200)

    def testCmdChagAppkey(self):
        u'''发送命令改变key'''
        self.assertEqual(self.SCMGI.sendCmdChagAppkeyMess(),200)

    def testgetUserHistory(self):
        u'''获取用户聊天历史记录'''
        self.assertEqual(self.SCMGI.getUserChatHistoryMess(),200)

    def testGetOfflineMessCout(self):
        u'''获取用户离线消息数目'''
        self.assertEqual(self.SCMGI.getOfflineMessCout(),200)

    def testChkOffliMessStat(self):
        u'''检查用户离线消息状态'''
        self.assertEqual(self.SCMGI.ChkOffliMessStat(),200)

    def testSendBCMess(self):
        u'''发送广播消息'''
        self.assertEqual(self.SCMGI.sendBroadcastMess(),200)

    def tearDown(self):
        self.SCMGI = None




