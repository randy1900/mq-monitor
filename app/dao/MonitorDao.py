#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Sep 24, 2015

@author: mountain
'''
from pymongo import MongoClient
from app.util import ConfUtil

client = MongoClient(ConfUtil.getMongoHost(), ConfUtil.getMongoPort())
db = client.mq_monitor
queue = db.queue
user = db.user

def saveQueue(data):
    queue.update({'queue': data.get('queue')}, data, upsert=True)

def findQueue(addr, queueName):
    return queue.find_one({'queue': queueName, 'addr': addr})
    
if __name__ == '__main__':
    print findQueue('c') == None