#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Sep 24, 2015

@author: mountain
'''

import requests
import json
from app.util import ConfUtil
from app.dao import MonitorDao
from app.mail import Mail
from requests.exceptions import ConnectionError
from app.util.LogUtil import log

class Monitor:
    
    def __init__(self):
        self.__addrList = ConfUtil.getMQAddrList()
        self.__username = ConfUtil.getMQUsername()
        self.__password = ConfUtil.getMQPassword()
    
    def check(self):
        mailContent = {}
        for mail in ConfUtil.getGlobalMailList():
            mailContent[mail.strip()] = [] 
        for addr in self.__addrList:
            overviewUrl = 'http://' + addr.strip() + '/api/overview'
            try:
                res = requests.get(overviewUrl, auth=(self.__username, self.__password))
            except ConnectionError, e:
                for mail in ConfUtil.getGlobalMailList():
                    mailContent[mail].append(addr + ' is dead.')
                continue
            queueUrl = 'http://' + addr.strip() + '/api/queues'
            res = requests.get(queueUrl, auth=(self.__username, self.__password))
            for queue in json.loads(res.text):
                queueName = queue.get('name')
                if queueName in ConfUtil.getIgnoreQueueList():
                    continue
                messages = queue.get('messages', 0)
                doc = MonitorDao.findQueue(addr, queueName)
                if doc == None:
                    if messages > ConfUtil.getGlobalMsgTotalMax():
                        alarm = addr + ', ' + queueName + ', ' + 'msgTotal is ' + str(messages) + '(' + str(ConfUtil.getGlobalMsgTotalMax()) + ').'    
                        for mail in ConfUtil.getGlobalMailList():
                            mailContent[mail].append(alarm)
                else:
                    try:
                        msgTotalMax = 0
                        if len(doc.get('msgTotalMax')) > 0:
                            msgTotalMax = (int)(doc.get('msgTotalMax'))
                    except Exception, e:
                        log.error(doc)
                    mailList = doc.get('mailList')
                    if messages > msgTotalMax:
                        alarm = addr + ', ' + queueName + ', ' + 'msgTotal is ' + str(messages) + '(' + str(msgTotalMax) + ').'
                        for mail in mailList:
                            if mailContent.get(mail) == None:
                                mailContent[mail] = []
                            mailContent[mail.strip()].append(alarm)
        Mail.sendMultiMail(mailContent)
        
if __name__ == '__main__':
    monitor = Monitor()
    monitor.check()