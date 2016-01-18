#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Sep 25, 2015

@author: mountain
'''
import requests
import json
from app.util import ConfUtil
from app.dao import MonitorDao

def subQueue(data):
    MonitorDao.saveQueue(data)

def getQueues(addr):
    queueUrl = 'http://' + addr.strip() + '/api/queues'
    res = requests.get(queueUrl, auth=(ConfUtil.getMQUsername(), ConfUtil.getMQPassword()))
    queues = []
    index = 0
    for queue in json.loads(res.text):
        queueName = queue.get('name')
        msgTotal = queue.get('messages', 0)
        dict = {}
        dict['queue'] = queueName
        dict['msgTotal'] = msgTotal
        index += 1
        dict['index'] = index
        doc = MonitorDao.findQueue(addr, queueName)
        dict['mailList'] = ''
        dict['msgTotalMax'] = ''
        if doc != None:
            dict['mailList'] = ','.join(doc.get('mailList'))
            dict['msgTotalMax'] = doc.get('msgTotalMax')
        queues.append(dict)
    return queues
