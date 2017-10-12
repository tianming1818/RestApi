#coding= utf-8
import sys
import unittest


sys.path.append("..")

from apiconfig import *
from Chatgroup.GetGroupInfo import *

class TestGetGroupsInfo(unittest.TestCase):
    def setUp(self):
        self.GIF = GroupsInfo(headers)

    def testGetAllGroup(self):
        u'''获取所有群组'''
        self.assertEqual(self.GIF.getAllGroups(),200)

    def testGetLimitGroup(self):
        u'''获取指定数量的群组'''
        self.assertEqual(self.GIF.getLimitGroups(),200)

    def testGetPubGroups(self):
        u'''获取所有公共群组'''
        self.assertEqual(self.GIF.getPublicGroups(),200)

    def testGetGroupDetail(self):
        u'''获取群组的详情'''
        self.assertEqual(self.GIF.getGroupDetail(),200)

    def tearDown(self):
        self.GIF = None