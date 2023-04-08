import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def send_email_by_qq(to):
    sender_mail = '邮箱'
    sender_pass = 'veejqthcbzhodeea'  # 同样是乱打的

    # 设置总的邮件体对象，对象类型为mixed
    msg_root = MIMEMultipart('mixed')
    # 邮件添加的头尾信息等
    msg_root['From'] = '邮箱<邮箱>'
    msg_root['To'] = to
    # 邮件的主题，显示在接收邮件的预览页面
    subject = 'XXX使用代码发送的第一封邮件，建议打开看看'
    msg_root['subject'] = Header(subject, 'utf-8')

    # # 构造文本内容
    # text_info = 'hello world'
    # text_sub = MIMEText(text_info, 'text/plain', 'utf-8')
    # msg_root.attach(text_sub)

    # 构造超文本
    url = "https://www.baidu.com"
    html_info = """
    <p>点击以下链接，你会去向一个更大的世界</p>
    <p><a href="%s">click me</a></p>
    <p>i am very galsses for you</p>
    """ % url
    html_sub = MIMEText(html_info, 'html', 'utf-8')
    # 如果不加下边这行代码的话，上边的文本是不会正常显示的，会把超文本的内容当做文本显示
    html_sub["Content-Disposition"] = 'attachment; filename="baidu.html"'
    # 把构造的内容写到邮件体中
    msg_root.attach(html_sub)

    # # 构造图片
    # image_file = open(
    #     r'E:\元气壁纸缓存\飞火\FFWallPaper\custom\samuraidoge\5a989f158267926702c5edfc34bda534_1_2_400x225.webp', 'rb').read()
    # image = MIMEImage(image_file)
    # image.add_header('Content-ID', '<image1>')
    # # 如果不加下边这行代码的话，会在收件方方面显示乱码的bin文件，下载之后也不能正常打开
    # image["Content-Disposition"] = 'attachment; filename="dog_want.png"'
    # msg_root.attach(image)
    #
    # # 构造附件
    # txt_file = open(r'F:\Java第一次实验课\Hello.java', 'rb').read()
    # txt = MIMEText(txt_file, 'base64', 'utf-8')
    # txt["Content-Type"] = 'application/octet-stream'
    # # 以下代码可以重命名附件为hello_world.txt
    # txt.add_header('Content-Disposition', 'attachment',
    #                filename='Hello.java')
    # msg_root.attach(txt)

    try:
        sftp_obj = smtplib.SMTP('smtp.qq.com', 25)
        sftp_obj.login(sender_mail, sender_pass)
        sftp_obj.sendmail(sender_mail, to, msg_root.as_string())
        sftp_obj.quit()
        print('sendemail successful!')

    except Exception as e:
        print('sendemail failed next is the reason')
        print(e)


if __name__ == '__main__':
    # 可以是一个列表，支持多个邮件地址同时发送，测试改成自己的邮箱地址
    to = '邮箱'
    send_email_by_qq(to)
