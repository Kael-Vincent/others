#coding=utf-8

import requests,json
from Setting.get_timestamp import get_timestamp


def get_signature(data):

    headers = {'content-type': 'application/json;charset=utf-8'}
    url = 'http://10.40.11.140:60000/openapi/getSignature?version=1.0&app_key=xcddsj2017&timestamp='+get_timestamp()
    r = requests.post(url,data=data,headers=headers)
    result=r.json()
    #print(result)
    return result['msg']
