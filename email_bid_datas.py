#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created Date: 2019-04-09
# Project     : export data to excel and email to 王帆

import sqlite3
import csv
import datetime

import smtplib
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def export_data_to_excel():
    with open('bid_data.csv', 'w+') as write_file:
        conn = sqlite3.connect('bid_datas.db')
        cur = conn.cursor()
        str_query_today_bid_datas = '''
                    select bid_title ,bid_title ,baidu_urls FROM bid_info WHERE bid_create_date=current_date ORDER BY bid_prov,bid_title;
                    '''
        # datas = cur.execute(str_query_today_bid_datas)
        # write_file.write(datas)
        # for row in cur.execute(str_query_today_bid_datas):
        #     print(row)
        #     write_file(cur.execute(str_query_today_bid_datas))
    
    with sqlite3.connect('bid_datas.db') as conn:
        csv_name = datetime.date.today().isoformat()+"_招标信息.csv"
        csvWriter = csv.writer(open(csv_name, "w" , encoding='gb2312'))
        cur = conn.cursor()
        str_query_today_bid_datas = '''
                    select bid_prov ,bid_title ,baidu_urls FROM bid_info WHERE bid_create_date=current_date ORDER BY bid_prov,bid_title;
                    '''
        cur.execute(str_query_today_bid_datas)
        rows = cur.fetchall()
        csvWriter.writerow(["省份","招标标题","百度链接"])
        csvWriter.writerows(rows)

        


def email_bid_datas():
    host_server = 'smtp.163.com'
    sender_163 = 'sinochemtech@163.com'
    #pwd为163邮箱的授权码
    pwd = 'sinochemtech123' ##
    #发件人的邮箱
    sender_163_mail = 'sinochemtech@163.com'
    #收件人邮箱
    receiver = '648569939@qq.com'

    #邮件的正文内容
    mail_content = "你好，<p>这是使用python登录qq邮箱发送HTML格式邮件的测试：</p><p><a href='http://www.yiibai.com'>test aaaaaaaa</a></p>"
    #邮件标题
    mail_title = '招标信息'

    #邮件正文内容
    msg = MIMEMultipart()
    #msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_163_mail
    msg["To"] = Header("接收者测试", 'utf-8') ## 接收者的别名

    #邮件正文内容
    msg.attach(MIMEText(mail_content, 'html', 'utf-8'))

    
    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(datetime.date.today().isoformat()+"_招标信息.csv", 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename=datetime.date.today().isoformat()+"_招标信息.csv"'
    msg.attach(att1)
    


    #ssl登录
    smtp = SMTP_SSL(host_server)
    #set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_163, pwd)

    smtp.sendmail(sender_163_mail, receiver, msg.as_string())
    smtp.quit()









if __name__ == '__main__':
    export_data_to_excel()
    email_bid_datas()