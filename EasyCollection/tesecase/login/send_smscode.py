import requests
import json
#import unittest
#class SendSmsCode(unittest.TestCase):
from Setting.common_setting import get_mobile

def test_send_code():
        # 初始化数据
        url = 'http://10.8.15.28:190/onecollection_app/send_sms_code'
        mobile=get_mobile()
        data = json.dumps({'mobile': mobile})
        print(mobile)
        headers = {'Content-Type': 'application/json;charset=utf-8'}
        try:
            r=requests.post(url, headers=headers, data=data)
            result=r.json()
            print(result)
        #son())
        except Exception as e:
            print(e)
        #finally:
            #print(result['code'])
            #return  result['code']

test_send_code()
#def tearDown(self):
        #pass
#if __name__ == '__main__':
    # unittest.main()
    #suite = unittest.TestSuite()
    #suite.addTest(SendSmsCode('test_send_code'))
    #runner = unittest.TextTestRunner()
    #runner.run(suite)