from Setting.test_e2j import _tongjiFirstRow

import json
import requests
import time
from Setting.get_timestamp import get_timestamp


def get_repayment_signature():
    #获取excel格式化数据
    data=_tongjiFirstRow()
    #print(data)
    timestamp=get_timestamp()
    headers = {'content-type': 'application/json;charset=utf-8','signature':'huiyhiyuio'}
    url='http://10.9.26.34:65000/openapi/getSignature?timestamp='+timestamp+'&version=1.0&app_key=dafyyd2018'
    print(url)
    r=requests.post(url,data=data,headers=headers)
    result=r.json()
    # print(result)
    signature=result['data']
    #print(signature)
    param=[]
    param.append(timestamp)
    param.append(signature)
    print(param)
    return param
get_repayment_signature()