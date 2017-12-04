#coding:utf-8

import sys
sys.path.append("..")
from apiconfig import *
true = True
false = False

userToken = {
    "grant_type": "password",
    "username": user1,
    "password": "1"
  }

cteUserBody = {"username":"rest116", "password":"1"}

cteMultiUsrBody = [{"username":"rest117","password":"1"},{"username":"rest118","password":"1"},{"username":"rest119","password":"1"},
                    {"username":"rest120","password":"1"},{"username":"rest121","password":"1"},
                   ]

setPWordBody = {"newpassword" : "2"}

nicknameBody = {"nickname": "new_name"}

MulUserStatBody = {"usernames":[user1,user2,user3]}

