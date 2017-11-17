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


if __name__ == "__main__":
    suite = unittest.TestSuite()
    try:
        rest = {
                #TestMessageTestCase:["testTM_1","testSendtwo_2","getfriend_3","testUpImage_4","testsendImage_5","testUpAudio_6","testsendAudio_7",
                #                     "testUpVideo_8", "testsendVideo_9","testsendNotic_10","testsendLoc_11","testForceNotifi_12","testPushTitle_13",
                #                     "testIgnoreNotifi_14","testPushBadge_15","testPushIgSound_16","testPushNewTitle_17"
                #                     ],
                #TestCallbackTestCase:["testAddCB_1","QueryCBs_2","QueryCBDetail_3","ModifyCB_4","DeleteCB_5"],
                #TestCmdMessageGetInfo:["testCmdMess_1","testCmdStartDebug_2","testCmdStopDebug_3","testCmdUploadLog_4","testCmdChagServer_5",
                #                    "testCmdChagAppkey_6","testgetUserHistory_7","testGetOfflineMessCout_8","testChkOffliMessStat_9",
                #                    "testSendBCMess_10"],
                #TestGetGroupsInfo:["testGetAllGroup_1","testGetLimitGroup_2","testGetPubGroups_3","testGetGroupDetail_4","testMultiGrpDetail_5",
                #                   "testGetGrpMember_6","testGetGrpBlkList_7","testJoinAllGrp_8","testMuteList_9","testadminList_10"],
                TestOperateGroup:["testPubGroup","testAddGrpMem","testMulGrpMem","testTrasnfer","testModiGrp","testDelGrpMem",
                                    "testDelMultiMem","testMembertoBlack","testMulMemtoBlack","testRmBlkMem","testRmBlkMultiMem",
                                  "testSendGrpMess",
                                  #"testDelGroup",
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
