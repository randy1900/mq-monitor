#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Sep 27, 2015

@author: mountain
'''
from app.util import ConfUtil
import smtplib
import requests
from email.mime.text import MIMEText
from email.header import Header
from app.util.LogUtil import log

fromAddr = ConfUtil.getFromAddr()
smtpServer = ConfUtil.getSmtpServer()
smtpPort = ConfUtil.getSmtpPort()
password = ConfUtil.getMailPassword()

def sendMail(toAddr, content):
    server = smtplib.SMTP(smtpServer, smtpPort)
    server.set_debuglevel(1)
    server.login(fromAddr, password)
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = Header(u'RabbitMQ报警', 'utf-8').encode()
    server.sendmail(fromAddr, toAddr, message.as_string())
    server.quit()

def sendMultiMail(data):
    print data
    try:
        server = smtplib.SMTP(smtpServer, smtpPort)
        server.set_debuglevel(1)
        server.login(fromAddr, password)
        for (mail, content) in data.items():
            if len(content) == 0:
                continue
            message = MIMEText('\n'.join(content), 'plain', 'utf-8')
            message['Subject'] = Header(u'RabbitMQ报警', 'utf-8').encode()
            server.sendmail(fromAddr, mail, message.as_string())
    except Exception, e:
        log.error(e)
    finally:
        server.quit()

if __name__ == '__main__':
    sendMail('shanqiu@in66.com', 'test')