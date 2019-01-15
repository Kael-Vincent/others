import requests,json
from qyweixin.GetAccessToken import get_access_token


def send_file():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+get_access_token()
    data = json.dumps({
        "touser":"yangyongqing",
        "msgtype": "file",
        "agentid": 1000009,
        "file": {
            "media_id": "D:/Users/yangyongqing/Desktop/gps.txt"
        },
        "safe": "0"
    })
    r = requests.post(url=url,data=data)
    result = r.json()
    print(result)

send_file()