#coding: utf-8

import requests,json
import datetime


url = "http://a1.easemob.com"
org = "easemob-demo"
app = "chatdemoui"
client_id = "YXA6TX5LoNxKEeOQ1eH_uqza9Q"
client_secret =  "YXA6DML6OxuXqwhjoetT7PX_eBQzg_M"
user1 = "online113"
user2 = "online112"
messages = "message from automation rest test"

#get before 3 days date
historymess = datetime.datetime.now() - datetime.timedelta(days=3)
olddate = historymess.strftime('%Y%m%d%H')


## get Admin token
def acquire_token(url,org,app,client_id,client_secret):
    tokenbody = {
        "grant_type": "client_credentials",
        "client_id": client_id ,
        "client_secret": client_secret
      }
    try:
        req = requests.post("%s/%s/%s/token" %(url,org,app),data=json.dumps(tokenbody),headers={'Content-Type': 'application/json'})
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


token,expires_in = acquire_token(url,org,app,client_id,client_secret)

print "Token is: %s, Expires_in is: %s" %(token,expires_in)


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

