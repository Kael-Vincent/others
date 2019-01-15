import time,sys
sys.path.append('./task_detail')
from HTMLTestRunner import HTMLTestRunner
import unittest
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import os


def send_mail(file_new):
    f=open(filename,'rb')
    mail_body=f.read()
    f.close()

    msg=MIMEText(mail_body,'html','utf-8')
    msg['Subject']=Header(u'易回接口测试报告','utf-8')
    smtp=smtplib.SMTP()
    smtp.connect('smtp.126.com')
    smtp.login('vincentyyq@126.com','yuanlang10240011')
    smtp.sendmail('vincentyyq@126.com','vincentyyq@126.com', msg.as_string())
    smtp.quit()
    print('email has send out !')


def new_report(testreport):
    lists=os.listdir(testreport)
    lists.sort(key=lambda  fn: os.path.getmtime(testreport+'\\'+fn))
    file_new=os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new


if __name__=='__main__':
    task_dir = 'D:/Users/yangyongqing/PycharmProjects/EasyCollection/debtor'
    test_report='D:/Users/yangyongqing/PycharmProjects/EasyCollection'
    discover = unittest.defaultTestLoader.discover(task_dir, pattern='*.py')
    print(discover)
    now=time.strftime("%Y-%m-%d %H-%M-%S")
    filename=now+'_result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='Tasks Detail',description='Get tasks detail:')
    runner.run(discover)
    fp.close()

    new_report=new_report(test_report)
    send_mail(new_report)
