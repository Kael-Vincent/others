from tesecase.message_repaire.get_signature import get_signature
from Setting.get_timestamp import get_timestamp
import requests
import json
#@author:Vincent
#日间活跃修复返回

def repaire_msg():
    url = 'http://10.40.11.140:60000/openapi/repairDebtorDayActiveAddr?app_key=xcddsj2017&version=1.0&timestamp='+get_timestamp()
    data = json.dumps({"returnCode": 1,
                       "data":
                           {
                               "lat": "22.538443",
                               "lng": "113.942624",
                               "cardNo": "393836198202269232"
                           }})
    headers = {'content-type': 'application/json;charset=utf-8','signature':get_signature(data)}
    r = requests.post(url,headers=headers,data=data)
    result = r.json()
    print(result)


repaire_msg()
