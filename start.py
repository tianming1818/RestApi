#coding= utf-8

import HTMLTestRunner as htr
import unittest
import sys,os

url = sys.argv[1]
org = sys.argv[2]
app = sys.argv[3]
username = sys.argv[4]
password = sys.argv[5]

os.system("python apiconfig.py %s %s %s %s %s" %(url,org,app,username,password))

from TestInspect.Callbacktest import *
from TestInspect.SendMessage import *
from TestInspect.SendCmdGetInfo import *
from TestInspect.verifyChatgroup import *
from TestInspect.verifyUserMan import *
from TestInspect.verifyChatroom import *
from TestInspect.verifyNotifier import *



if __name__ == "__main__":
    suite = unittest.TestSuite()
    try:
        rest = {
                TestMessageTestCase:["testTM_1","testSendtwo_2","getfriend_3","testUpImage_4","testsendImage_5","testUpAudio_6","testsendAudio_7",
                                     "testUpVideo_8", "testsendVideo_9","testsendNotic_10","testsendLoc_11","testForceNotifi_12","testPushTitle_13",
                                     "testIgnoreNotifi_14","testPushBadge_15","testPushIgSound_16","testPushNewTitle_17",
                                     ],
                TestCallbackTestCase:["testAddCB_1","QueryCBs_2","QueryCBDetail_3","ModifyCB_4","DeleteCB_5",
                                      ],
                TestCmdMessageGetInfo:["testCmdMess_1","testCmdStartDebug_2","testCmdStopDebug_3","testCmdUploadLog_4","testCmdChagServer_5",
                                    "testCmdChagAppkey_6","testgetUserHistory_7","testGetOfflineMessCout_8","testChkOffliMessStat_9",
                                    "testSendBCMess_10",
                                    ],
                TestGetGroupsInfo:["testGetAllGroup_1","testGetLimitGroup_2","testGetPubGroups_3","testGetGroupDetail_4","testMultiGrpDetail_5",
                                   "testGetGrpMember_6","testGetGrpBlkList_7","testJoinAllGrp_8","testMuteList_9","testShareFileList_10","testadminList_11",
                                  ],
                TestOperateGroup:["testPubGroup_1","testAddGrpMem_2","testMulGrpMem_3","testTrasnfer_4","testModiGrp_5","testDelGrpMem_6",
                                  "testDelMultiMem_7","testMembertoBlack_8","testMulMemtoBlack_9","testRmBlkMem_10","testRmBlkMultiMem_11",
                                  "testSendGrpMess_12","testMuteMem_13","testunMuteMem_14","testAddAdmin_15","testDelAdmin_16","testApplyJoinGrp_17",
                                  "testDelGroup_18","testCrePubVerifyGrp_19","testVerifyAlyJoin_20","testCtePrivateGrp_21","testPriSendMess_22",
                                  "testPriAllowInvite_23","testLeaveGroup_24",
                                  ],
                TestChatRoom:["testCteroom_1","testGetAllRoom_2","testModifyRoom_3","testRoomDetail_4","testInviteMem_5","testInvtMulMem_6",
                              "testKickMemRoom_7","testKickMulMem_8","testJoinAllRooms_9","testGetAllRobot_10","testSendMessRoom_11",
                              "testAddRoomAdmin_12","testgetAdminList_13","testRmRoomAdmin_14","testMuteMembet_15","testGetMuteList_16",
                              "testRmMuteMember_17","testDelChatroom_18",
                              ],
                TestUserManage:["testClitSecret_1","testGetAdmToken_2","testUserToken_3","testGetAllUser_4","testCrteUser_5","testCteMulUser_6",
                                "testGetUsrDetail_7","testMulUsrDetail_8","testChkOnlineStat_9","testDelUser_10",
                                #"testDelMulUser_11",
                                "testResetPword_12","testModNickname_13","testAddFriend_14","testDelFriend_15","testGetFridList_16",
                                "testMvToBlack_17","testGetBlackList_18","testRmBlkList_19","testDeactivUser_20","testActivUser_21",
                                "testDsconnectUser_22",
                                ],
                TestNotifiers: ["testGetNotifier_1","testUpNotifiHuaW_2","testDelHuaWeiNoti_3","testUpXiaoMiNoti_4",
                                "testDelXizoMiNotifi_5",
                                ],
                }
        for classes,methlist in rest.items():
            for methods in methlist:
                suite.addTest(classes(methods))

    except ValueError,e:
        print "your methodname is not exist: %s" % e

    filename = '%s/logs/index.html' % os.getcwd()
    fp = file(filename,'wb')
    runner=htr.HTMLTestRunner(
        stream=fp,
        title='Easemob Test Report',
        description='REST API test report')
    runner.run(suite)
