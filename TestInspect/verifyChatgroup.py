#coding= utf-8
import sys
import unittest


sys.path.append("..")

from apiconfig import *
from Chatgroup.proChatgroup import *
from Chatgroup.bodyfile import *

class TestGetGroupsInfo(unittest.TestCase):
    def setUp(self):
        self.GIF = GroupsInfo(headers)

    def testGetAllGroup_1(self):
        u'''获取所有群组'''
        self.assertEqual(self.GIF.getAllGroups(),200)
    def testGetLimitGroup_2(self):
        u'''获取指定数量的群组'''
        self.assertEqual(self.GIF.getLimitGroups(),200)
    def testGetPubGroups_3(self):
        u'''获取所有公共群组'''
        self.assertEqual(self.GIF.getPublicGroups(),200)
    def testGetGroupDetail_4(self):
        u'''获取群组的详情'''
        self.assertEqual(self.GIF.getGroupDetail(),200)
    def testMultiGrpDetail_5(self):
        u'''获取多个群组的详情'''
        self.assertEqual(self.GIF.getMultiGrpDetail(),200)
    def testGetGrpMember_6(self):
        u'''获取群组成员'''
        self.assertEqual(self.GIF.getGroupMember(),200)
    def testGetGrpBlkList_7(self):
        u'''获取群组黑名单列表'''
        self.assertEqual(self.GIF.getGrpBlacklit(),200)
    def testJoinAllGrp_8(self):
        u'''获取用户加入所有的群'''
        self.assertEqual(self.GIF.getjoinAllGrp(),200)
    def testMuteList_9(self):
        u'''获取群的禁言列表'''
        self.assertEqual(self.GIF.getmutelist(),200)
    def testadminList_10(self):
        u'''获取群管理员列表'''
        self.assertEqual(self.GIF.getAdminlist(),200)

    def tearDown(self):
        self.GIF = None

class TestOperateGroup(unittest.TestCase):
    def setUp(self):
        self.OpG = OperateGroup(headers,CrePubGrpBody,multiMemBody,grpTransBody,modgrpBody,mulMemtoblackBody)
    def testPubGroup(self):
        u'验证创建公共群组'
        global groupid
        result, groupid = self.OpG.CrePubGrp()
        self.assertTrue(result,True)
    def testAddGrpMem(self):
        u'验证增加群成员'
        self.assertEqual(self.OpG.groupAddMem(groupid),200)
    def testMulGrpMem(self):
        u'验证增加多个群成员'
        self.assertEqual(self.OpG.GrpAddMulMem(groupid),200)
    def testTrasnfer(self):
        u'验证群主转让'
        self.assertEqual(self.OpG.GrpTransfer(groupid),200)
    def testModiGrp(self):
        u'验证群组修改'
        self.assertEqual(self.OpG.modifyGrp(groupid),200)
    def testDelGrpMem(self):
        u'验证删除一个群成员'
        self.assertEqual(self.OpG.delGrpMem(groupid),200)
    def testDelMultiMem(self):
        u'验证删除多个群成员'
        self.assertEqual(self.OpG.delMultiMem(groupid),200)
    def testMembertoBlack(self):
        u'验证将成员移入黑名单'
        self.OpG.groupAddMem(groupid)
        self.OpG.GrpAddMulMem(groupid)
        self.assertEqual(self.OpG.MemToBlack(groupid),200)
    def testMulMemtoBlack(self):
        u'验证将多成员移入黑名单'
        self.assertEqual(self.OpG.MultiMemToBlack(groupid),200)
    def testRmBlkMem(self):
        u'验证将好友从黑名单中移除'
        self.assertEqual(self.OpG.RmBlackMem(groupid),200)
    def testRmBlkMultiMem(self):
        u'验证将多个成员从黑名单移除'
        self.assertEqual(self.OpG.RmBlkMultiMem(groupid),200)
    def testSendGrpMess(self):
        u'验证发送群消息'
        self.assertEqual(self.OpG.sendGrpMess(groupid),200)




    def testDelGroup(self):
        u'验证删除群组'
        self.assertEqual(self.OpG.MemToBlack(groupid),200)
    def tearDown(self):
        self.OpG = None
