#coding= utf-8
import sys
import unittest


sys.path.append("..")

from apiconfig import *
from Callback.OpertCallbak import *


class TestCallbackTestCase(unittest.TestCase):
    def setUp(self):
        self.CB = HxCallback(headers,addbody,modifybody)

    def testAddCB(self):
        u'''新增一个Callback'''
        self.assertEqual(self.CB.addcallback(),200)

    def QueryCBs(self):
        u'''查询Callback'''
        self.assertEqual(self.CB.querycallbacks(),200)

    def QueryCBDetail(self):
        u'''查询一个Callback祥情'''
        self.assertEqual(self.CB.queryCBDetail(),200)

    def ModifyCB(self):
        u'''修改一个Callback'''
        self.assertEqual(self.CB.modifyCB(),200)

    def DeleteCB(self):
        u'''删除一个Callback'''
        self.assertEqual(self.CB.deleteCB(),200)

    def tearDown(self):
        self.CB = None