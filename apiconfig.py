#coding: utf-8

import requests,json
import datetime,sys


url = sys.argv[1]
org = sys.argv[2]
app = sys.argv[3]
username = sys.argv[4]
password = sys.argv[5]


user1 = "rest111"
user2 = "rest112"
user3 = "rest113"
user4 = "rest114"
user5 = "rest115"
messages = "message from automation rest test"


#get before 3 days date
historymess = datetime.datetime.now() - datetime.timedelta(days=3)
olddate = historymess.strftime('%Y%m%d%H')


## get Admin token
def acquire_token(url,username,password):
    tokenbody = {
        "grant_type":"password",
        "username":username,
        "password":password }
    try:
        req = requests.post("%s/management/token" %(url),data=json.dumps(tokenbody),headers={'Accept':'application/json','Content-Type': 'application/json'})
    except requests.exceptions.ConnectionError,e:
        return "Your url is error :", e.message
    try:
        if req.status_code == 200:
            contents = json.loads(req.content)
            tokens = contents["access_token"]
            expires_in = contents["expires_in"]
            return tokens,expires_in
        else:
            return req.status_code,req.content
    except UnboundLocalError,e:
        return e,e.message


token,expires_in = acquire_token(url,username,password)

#print "Token is: %s, Expires_in is: %s" %(token,expires_in)


headers = {'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': "Bearer %s" % token}


def ornament(func):
    def judge(*args, **kwargs):
        try:
            r = func(*args, **kwargs)
            data = r.json()
            print json.dumps(data, sort_keys=True, indent=2)
        except TypeError, e:
            return "your url is error: %s" % e
        if r.status_code != 200:
            return r.status_code,r.content
        else:
            return r.status_code
    return judge

