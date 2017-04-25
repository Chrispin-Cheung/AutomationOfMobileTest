# -*- coding:UTF-8 -*-

#Author:iotrookie
#CreateTime:2017.04.12
#Funciton: 发送Email
#Edit:
#Edit Author:
#Edit CreateTime:
#Edir Function:


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class SendEmailModel(object):
    def MKEmailSiteDriver(self,fileName):
        sender = 'rsmb2008@163.com'
        receiver ='543622565@qq.com'#自己邮箱地址
        subject = 'test reporter'
        smtpserver = 'smtp.163.com'
        username = 'rsmb2008@163.com'
        password = 'kpNOVA9293AI1314'

        msgRoot = MIMEMultipart('related')
        msgRoot['From'] = '<rsmb2008@163.com>'
        msgRoot['To'] = "543622565@qq.com"
        msgRoot['Subject'] = subject
        text_msg = MIMEText("<html><body><p><span style='color: red'>&nbsp;&nbsp; hi all:</span></p><p>&nbsp;&nbsp;&nbsp;&nbsp;附件为本次回归测试报告，请各位查收!哈哈哈</br></p></body></html>",'html','utf-8')
        msgRoot.attach(text_msg)
        #构造附件
        att = MIMEText(open('../TestWeatherReport/'+fileName, 'rb').read(), 'base64', 'utf-8')#需要更改文件路径
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="reporter.htm"'
        msgRoot.attach(att)

        smtp = smtplib.SMTP()
        try:
            smtp.connect(host=smtpserver,port='25')
            smtp.login(username,password)
            smtp.sendmail(sender,receiver,msgRoot.as_string())
            smtp.quit()
        except Exception:
            assert False,\
                "发送失败"
