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
    def testShareFileList_10(self):
        u'获取群共享文件列表'
        self.assertEqual(self.GIF.ShareFilelist(),200)
    def testadminList_11(self):
        u'''获取群管理员列表'''
        self.assertEqual(self.GIF.getAdminlist(),200)

    def tearDown(self):
        self.GIF = None

class TestOperateGroup(unittest.TestCase):
    def setUp(self):
        self.OpG = OperateGroup(headers,CrePubGrpBody,multiMemBody,grpTransBody,modgrpBody,mulMemtoblackBody,muteMemBody,
                                addAdminBody,pubGrpVerifyBody,verifyBody,privateBody,privateAllowBody)
    def testPubGroup_1(self):
        u'验证创建公共群组'
        global groupid
        result, groupid = self.OpG.CrePubGrp()
        self.assertTrue(result,True)
    def testAddGrpMem_2(self):
        u'验证增加群成员'
        self.assertEqual(self.OpG.groupAddMem(groupid),200)
    def testMulGrpMem_3(self):
        u'验证增加多个群成员'
        self.assertEqual(self.OpG.GrpAddMulMem(groupid),200)
    def testTrasnfer_4(self):
        u'验证群主转让'
        self.assertEqual(self.OpG.GrpTransfer(groupid),200)
    def testModiGrp_5(self):
        u'验证群组修改'
        self.assertEqual(self.OpG.modifyGrp(groupid),200)
    def testDelGrpMem_6(self):
        u'验证删除一个群成员'
        self.assertEqual(self.OpG.delGrpMem(groupid),200)
    def testDelMultiMem_7(self):
        u'验证删除多个群成员'
        self.assertEqual(self.OpG.delMultiMem(groupid),200)
    def testMembertoBlack_8(self):
        u'验证将成员移入黑名单'
        self.OpG.groupAddMem(groupid)
        self.OpG.GrpAddMulMem(groupid)
        self.assertEqual(self.OpG.MemToBlack(groupid),200)
    def testMulMemtoBlack_9(self):
        u'验证将多成员移入黑名单'
        self.assertEqual(self.OpG.MultiMemToBlack(groupid),200)
    def testRmBlkMem_10(self):
        u'验证将好友从黑名单中移除'
        self.assertEqual(self.OpG.RmBlackMem(groupid),200)
    def testRmBlkMultiMem_11(self):
        u'验证将多个成员从黑名单移除'
        self.assertEqual(self.OpG.RmBlkMultiMem(groupid),200)
    def testSendGrpMess_12(self):
        u'验证发送群消息'
        self.OpG.groupAddMem(groupid)
        self.OpG.GrpAddMulMem(groupid)
        self.assertEqual(self.OpG.sendGrpMess(groupid),200)
    def testMuteMem_13(self):
        u'验证对群成员禁言'
        self.assertEqual(self.OpG.MuteMember(groupid),200)
    def testunMuteMem_14(self):
        u'验证对禁言成员解禁言'
        self.assertEqual(self.OpG.unMuteMember(groupid),200)
    def testAddAdmin_15(self):
        u'验证增一个群管理员'
        self.assertEqual(self.OpG.addAdmin(groupid),200)
    def testDelAdmin_16(self):
        u'验证删除一个群管理员'
        self.OpG.delGrpMem(groupid)
        self.assertEqual(self.OpG.delAdmin(groupid), 200)
    def testApplyJoinGrp_17(self):
        u'验证申请加入群组'
        self.assertEqual(self.OpG.ApplyJoinGrp(groupid),200)
    def testDelGroup_18(self):
        u'验证删除群组'
        self.assertEqual(self.OpG.deleteGroup(groupid),200)
    def testCrePubVerifyGrp_19(self):
        u'验证创建需要审批的公开群'
        global PubVerifyID
        result,PubVerifyID = self.OpG.CrePubVerify()
        self.assertTrue(result, True)
        self.OpG.ApplyJoinGrp(PubVerifyID)
    def testVerifyAlyJoin_20(self):
        u'验证审批申请加入的公开群'
        self.assertEqual(self.OpG.vefyAlyJoinGrp(PubVerifyID),200)
        self.OpG.deleteGroup(PubVerifyID)
    def testCtePrivateGrp_21(self):
        u'验证创建私有群'
        global PrivateID
        result,PrivateID = self.OpG.CrePrivateGrp()
        self.assertTrue(result,True)
    def testPriSendMess_22(self):
        u'验证私有群添加成员并发送消息'
        self.OpG.groupAddMem(PrivateID)
        self.OpG.GrpAddMulMem(PrivateID)
        self.assertEqual(self.OpG.sendGrpMess(PrivateID), 200)
        self.OpG.deleteGroup(PrivateID)
    def testPriAllowInvite_23(self):
        u'验证创建允许邀请的私有情'
        global PriAllowInID
        result,PriAllowInID = self.OpG.CtePrivAllowGrp()
        self.assertTrue(result,True)
        self.OpG.groupAddMem(PriAllowInID)
    def testLeaveGroup_24(self):
        u'验证退出群组'
        self.assertEqual(self.OpG.LeaveGroup(PriAllowInID),200)
        self.OpG.deleteGroup(PriAllowInID)


    def tearDown(self):
        self.OpG = None
