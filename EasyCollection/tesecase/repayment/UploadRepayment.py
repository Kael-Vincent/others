import requests
from Setting.test_e2j import  _tongjiFirstRow
from tesecase.repayment.GetRepaymentSignature import get_repayment_signature
from requests import ConnectionError

def uploadRepayment():
    t_s=get_repayment_signature()
    timestamp=t_s[0]
    signature=t_s[1]
    data=_tongjiFirstRow()
    print(data)
    #signature= tesecase.repayment.GetRepaymentSignature.get_repayment_signature()
    headers = {'content-type': 'application/json;charset=utf-8','signature':signature}
    url='http://collection.first.test.com/openapi/uploadRepayments?timestamp='+timestamp+'&version=1.0&app_key=dafyyd2018'
    try:
        r = requests.post(url,data=data,headers=headers)
        result = r.json()
        print(result)
    except ConnectionError as ce:
        print('连接失败')


if __name__ == '__main__':
    uploadRepayment()