# coding=utf-8

import json
import unittest

import requests
from tesecase.login.GetSms import getSms
from Setting.common_setting import get_mobile


class LoginTest(unittest.TestCase):
    def setUp(self):
        # 初始化数据
        self.base_url = 'http://10.8.15.65:60001/onecollection_app/login'
        self.passwd=getSms.test_getSms(self)
        self.data = json.dumps({'account': get_mobile(), 'passwd': self.passwd})
        self.headers = {'Content-Type': 'application/json;charset=UTF-8'}

    def test_login(self):
        # 登录
        try:
            r = requests.post(url=self.base_url, data=self.data, headers=self.headers)
            result = r.json()
            print(result)
            self.assertEqual(result['code'], 0)
            session = result['data']['session_key']
            print(session)
            self.assertEqual(result['subCode'], 0)
            print(session)
            sum=0
            f = open("D:/Users/yangyongqing/PycharmProjects/EasyCollection/src/save_session.txt", 'r+')
            # print(session)
            f.write(session)
            f.close()
        except Exception as e:
            print(e)
            sum = 1
        if sum == 0:
            print('test bingo')
        else:
            print('test failed')

    def tearDown(self):
        print('test ended')



if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(LoginTest('login_test'))
    #sssuite.addTest(LoginTest('print_cookie'))
    # suite.addTest(Update_Staff_Status_Test('Status_Update_Test'))
    runner = unittest.TextTestRunner()
    runner.run(suite)






