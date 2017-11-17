#coding:utf-8

import sys
sys.path.append("..")
from apiconfig import *
true = True
false = False

CrePubGrpBody = {
    "groupname":"public_group",
    "desc":"RST created group",
    "public":true,
    "maxusers":800,
    "approval":false,
    "owner":user1,
    "members":[user2]
}

multiMemBody = {"usernames":[user4,user5]}

grpTransBody = {"newowner":user2}

modgrpBody = {
    "groupname":"group update",
    "description":"updategroupinfo",
    "maxusers":300
}

mulMemtoblackBody = {"usernames":[user4,user5]}