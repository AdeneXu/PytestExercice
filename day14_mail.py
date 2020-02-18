from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import parseaddr,formataddr
from email.mime.base import MIMEBase


def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

def mail():
    from_addr = 'adene_xu@163.com'
    to_addr = 'adene_xu@163.com'
    message = MIMEText('用python发送邮件的示例代码.','plain','utf-8')
    message['From'] = _format_addr('貂蝉 <%s>' % from_addr)
    message['To'] = _format_addr('妲己 <%s>' % to_addr)
    message['Subject'] = Header('练习邮件发送和接收','utf-8')
    smtper = SMTP('smtp.163.com',25)
    smtper.login(from_addr,'2020XF')
    smtper.sendmail(from_addr,[to_addr],message.as_string())
    print('邮件发送成功')

def mail_attach():
    #创建一个带附件的邮件消息对象
    message = MIMEMultipart()

    from_addr = 'adene_xu@163.com'
    to_addr = 'adene_xu@163.com'
    message['From'] = _format_addr('貂蝉 <%s>' % from_addr)
    message['To'] = _format_addr('妲己 <%s>' % to_addr)

    #创建文本内容
    text_content = MIMEText('带附件发送邮件','plain','utf-8')
    message['Subject'] = Header('练习附件发送','utf-8')
    #将文本内容添加到邮件消息对象中
    message.attach(text_content)

    #读取文件并将文件作为附件添加到邮件消息对象中
    with open('C:/Users/Administrator/Desktop/教师资格证.txt','rb') as f:
        txt = MIMEText(f.read(),'base64','utf-8')
        txt.add_header('Content-Type','text/plain')
        txt.add_header('Content-Disposition','attachment',filename='教师资格证.txt')
        message.attach(txt)
    #读取文件并将文件作为附件添加到邮件消息对象中
    with open('C:/Users/Administrator/Desktop/新建.xls','rb') as f:
        xls = MIMEText(f.read(),'base64','utf-8')
        xls.add_header('Content-Type','application/octet-stream')
        xls.add_header('Content-Disposition','attachment',filename='新建.xls')
        message.attach(xls)

    #创建SMTP对象
    smpter = SMTP('smtp.163.com')
    #开启安全连接
    # smpter.starttls()
    sender = 'adene_xu@163.com'
    receivers = ['adene_xu@163.com']
    #登录到SMTP服务器
    smpter.login(sender,'2020XF')
    smpter.sendmail(sender,receivers,message.as_string())
    smpter.quit()
    print('发送完成')

if __name__ == '__main__':
    # mail()
    mail_attach()