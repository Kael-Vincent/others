import requests


def get_access_token():
    corpid = "wwd6795843b6564b81"
    corpsecret = "O0MlGsAuFb-ABs_hYPKzmmE4H-YXnBeRc79naE7aS-o"
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?"+"corpid="+corpid+"&corpsecret="+corpsecret
    r = requests.get(url)
    result = r.json()['access_token']
    print(result)
    return result

