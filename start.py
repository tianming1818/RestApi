#coding= utf-8

import HTMLTestRunner as htr
import unittest
import sys


from TestInspect.Callbacktest import *
from TestInspect.SendMessage import *
from TestInspect.SendCmdGetInfo import *
from TestInspect.CKgetGroups import *


if __name__ == "__main__":
    suite = unittest.TestSuite()
    try:
        rest = {
                TestMessageTestCase:["testTM","testSendtwo","getfriend","testsendImage","testsendAudio",
                                     "testsendVideo","testsendNotic","testsendLoc","testForceNotifi","testPushTitle",
                                     "testIgnoreNotifi","testPushBadge","testPushIgSound","testPushNewTitle"],
                TestCallbackTestCase:["testAddCB","QueryCBs","QueryCBDetail","ModifyCB","DeleteCB"],
                TestCmdMessageGetInfo:["testCmdMess","testCmdStartDebug","testCmdStopDebug","testCmdUploadLog","testCmdChagServer",
                                       "testCmdChagAppkey","testgetUserHistory","testGetOfflineMessCout","testChkOffliMessStat",
                                       "testSendBCMess"],
                TestGetGroupsInfo:["testGetAllGroup","testGetLimitGroup","testGetPubGroups","testGetGroupDetail"],
                }
        for classes,methlist in rest.items():
            for methods in methlist:
                suite.addTest(classes(methods))

    except ValueError,e:
        print "your methodname is not exist: %s" % e

    filename = '../logs/test.html'
    fp = file(filename,'wb')
    runner=htr.HTMLTestRunner(
        stream=fp,
        title='Easemob Test Report',
        description='REST API test report')
    runner.run(suite)
