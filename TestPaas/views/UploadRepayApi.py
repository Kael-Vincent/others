from flask import Flask
from flask_restful import reqparse, Api, Resource
import json,requests,time


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('repay',type=str,action='append')

t = time.time()
timestamp = str(round(t * 1000))


def get_signature(*args):
    data=json.dumps(args)
    url = 'http://10.40.11.140:65500/openapi/uploadRepayments?timestamp=' + timestamp + '&version=1.0&app_key=18510000002'
    headers = {'content-type': 'application/json;charset=utf-8'}
    r = requests.post(url, data=data, headers=headers)
    result = r.json()
    signature = result['data']
    print(signature)
    return signature


def upload_repay(*args):
    data=json.dumps(args)
    url='http://collection.first.test.com/openapi/uploadRepayments?timestamp='+timestamp+'&version=1.0&app_key=18510000002'
    signature = get_signature()
    headers = {'content-type': 'application/json;charset=utf-8','signature':signature}
    r=requests.post(url,data=data,headers=headers)
    result=r.json()
    return result


class UploadRepay(Resource):
    def post(self):
        args = parser.parse_args()
        res = upload_repay(args)
        return res,201


api.add_resource(UploadRepay,'/upload_repay')

## Actually setup the Api resource routing here


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)