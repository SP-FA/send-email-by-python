import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


class Mail:
    def __init__(self, host, userName, pwd):
        self.imgLst = []
        self.fileLst = []
        try:
            if 'qq' in host:
                self.smtpObj = smtplib.SMTP_SSL(host)
            else:
                # 启动
                self.smtpObj = smtplib.SMTP()
                # 连接到服务器
                self.smtpObj.connect(host, 25)
            self.smtpObj.login(userName, pwd) 
            print('e-mail account log in successful!')
        except smtplib.SMTPException as e:
            print('Error: ', e)


    def send(self, msg, title, sender, receivers):
        message = MIMEMultipart()
        message['Subject'] = title
        message['From'] = sender
        message['To'] = ','.join(receivers)

        content = MIMEText(msg, 'plain', 'utf-8')
        message.attach(content)

        for i in self.imgLst:
            message.attach(i)

        for i in self.fileLst:
            message.attach(i)

        try:
            self.smtpObj.sendmail(sender, receivers, message.as_string())
            print('message send successful!')
        except smtplib.SMTPException as e:
            print('Error: ', e)


    def add_img(self, imgPath, imgName):
        with open(imgPath, 'rb') as fp:
            img = MIMEImage(fp.read())
        img['Content-Type'] = 'application/octet-stream'
        img['Content-Disposition'] = 'attachment;filename="%s"' % (imgName)
        self.imgLst.append(img)


    def add_file(self, fPath, fileName):
        with open(fPath, 'rb') as fp:
            content = fp.read()
        f = MIMEText(content, 'plain', 'utf-8')
        f['Content-Type'] = 'application/octet-stream'
        f['Content-Disposition'] = 'attachment;filename="%s"' % (fileName)
        self.fileLst.append(f)


    def logout(self):
        self.smtpObj.quit()


if __name__ == '__main__':
    # 设置服务器所需信息
    # 邮箱服务器地址
    mail_host = 'smtp.qq.com'  
    # 用户名
    mail_user = '2053232384'
    # 密码(部分邮箱为授权码) 
    mail_pass = 'syktappnjddlcadd'

    sender = ''
    receivers = ['']
    message = "ztrmyxdd"
    imagePath = "./pite.png"
    filePath = "./test.csv"
    
    email = Mail(mail_host, mail_user, mail_pass)
    email.add_file(filePath, "test.csv")
    email.add_img(imagePath, "piteCry.png")
    email.send(message, '测试使用python发邮件', sender, receivers)
