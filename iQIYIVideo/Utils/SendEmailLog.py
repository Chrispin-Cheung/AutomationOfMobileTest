#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class sendEmailModel(object):
    def MKEmailSiteDriver(self,fileName):
        sender = '976509004@qq.com'
        receiver ='guo_huahsag@163.com'#自己邮箱地址
        #多人群发时，receiver ＝ ［“smith@163.com”，“yeah@163.com”，“puzzle@163.com”］
        subject = 'test reporter'
        smtpserver = 'smtp.qq.com'
        username = '976509004@qq.com'
        password = '!@#$%^&'

        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = subject
        text_msg = MIMEText("<html><body><p><span style='color: red'>;&nbsp;&nbsp; hi all:</span></p><p>&nbsp;&nbsp;&nbsp;&nbsp;附件为本次回归测试报告，请各位查收!</br></p></body></html>",'html','utf-8')
        msgRoot.attach(text_msg)
        #构造附件
        att = MIMEText(open('../TestJikeReport/'+fileName, 'rb').read(), 'base64', 'utf-8')#需要更改文件路径
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="reporter.htm"'
        msgRoot.attach(att)


        smtp = smtplib.SMTP()
        try:
            smtp.connect(host=smtpserver,port='25')   #smtp  服务端口固定 为25 qq的stmp端口号为465
            smtp.login(username,password)
            smtp.sendmail(from_addr=sender,to_addrs=receiver,msg=msgRoot.as_string())
            smtp.quit()
        except Exception:
            assert False,\
                "发送失败"