import requests
import json
import sendNotify
from os import environ, system

# import telepot

#Api信息
rain_api_key = ''

rain_api_key = environ.get("rain_api_key") if environ.get("rain_api_key") else ""


#请求用户信息
url = "https://api.v2.rainyun.com/user/"
payload={}
headers_yh = {
   'X-Api-Key':rain_api_key
}
res_points = requests.request("GET", url, headers=headers_yh, data=payload)
zh_json = res_points.json()
pointsbefore = zh_json['data']['Points']
ID = zh_json['data']['ID']
name = zh_json['data']['Name']
print(f'ID：{ID}')
print(f'用户名：{name}')
print(f'剩余积分：{pointsbefore}')
print('==============================')
#签到部分
url_lqjf = 'https://api.v2.rainyun.com/user/reward/tasks'
headers_lqjf = {
    'content-type':"application/json",
    'X-Api-Key':rain_api_key
    }
body_lqjf = {
    "task_name" : '每日签到',
    "verifyCode" : ''
    }
res_points = requests.request("GET", url, headers=headers_yh, data=payload)
res_lqjf = requests.request("POST", url_lqjf, headers=headers_lqjf, data = json.dumps(body_lqjf))
zh_json = res_points.json()

points = zh_json['data']['Points']
if points == {pointsbefore + 300}:
# if res_lqjf.text.data == 'ok':
    print(f'签到成功，当前剩余积分：{points + 300}')
else:
    print(f'签到失败，返回值：{res_lqjf.text}')
print('==============================')
#推送

sendmessage = '''雨云自动签到Bot\n签到通知\n用户ID：{0}\n用户名：{1}\n签到前积分：{2}\n当前积分：{3}\nhttps://github.com/ZYGLQexplorer/RainYun-Checkin'''.format(ID, name, pointsbefore, points)
sendNotify.send('雨云签到',sendmessage)
