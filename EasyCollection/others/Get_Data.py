import json
import unittest
import time


class Get_openapi_url(unittest.TestCase):
    def setUp(self):
        c = time.time()
        timestamp = str(round(c * 1000))
        print(timestamp)
        self.base_url='http://10.8.15.65:65500/openapi/uploadRepayments?'+timestamp+'&version=1.0&app_key=18510000001'

    def test_get_url(self):
        try:
            url=self.base_url
            print(url)
        except Exception as e:
            print(e)
    def tearDown(self):
        pass


if __name__=="__main__":
    unittest.main()
'''t=Get_openapi_url()
t.setUp()
t.Test_get_url()'''


