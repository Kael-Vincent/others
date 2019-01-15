
import redis

from tesecase.login.send_smscode import test_send_code
from Setting.common_setting import get_mobile
import unittest

class getSms(unittest.TestCase):

    def setUp(self):
        pass
    def test_getSms(self):
        # sms= test_send_code()
        # if sms==0:
        #     print ('发送验证码成功')
        # else:
        #     print('发送验证码失败')
        try:
            r=redis.Redis(host='10.8.15.65', port=6479, db=0, password='Hqk170619')
            code = r.get('login_sms_code:'+get_mobile()+'_3')
            print(code)
        except Exception as e:
            print(e)
        finally:
            print(int(code))
            return int(code)

        def tearDown(self):
            pass



    def query_session():
        r = redis.Redis(host='10.8.15.65', port=6479, db=0, password='Hqk170619')
        session=r.get('login_user:581')
        print(session)

if __name__=='__main__':
    unittest.main()