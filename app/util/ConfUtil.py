#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Sep 24, 2015

@author: mountain
'''
import ConfigParser
import os

parser = ConfigParser.ConfigParser()
parser.read(os.getcwd().split('mq-monitor')[0] + 'mq-monitor/conf/env.ini')

def getMQAddrList():
    return parser.get('mq', 'addr').strip().split(',')

def getMQUsername():
    return parser.get('mq', 'username').strip()

def getMQPassword():
    return parser.get('mq', 'password').strip()

def getMongoHost():
    return parser.get('mongo', 'host').strip()

def getMongoPort():
    return int(parser.get('mongo', 'port').strip())

def getGlobalMsgTotalMax():
    return int(parser.get('global', 'msgTotalMax'))

def getGlobalMailList():
    return parser.get('global', 'mailList').strip().split(',')

def getIgnoreQueueList():
    return parser.get('global', 'ignoreQueueList').strip().split(',')

def getFromAddr():
    return parser.get('mail', 'fromAddr').strip()

def getMailPassword():
    return parser.get('mail', 'password').strip()

def getSmtpServer():
    return parser.get('mail', 'smtpServer').strip()

def getSmtpPort():
    return int(parser.get('mail', 'smtpPort').strip())

def getPostUrl():
    return parser.get('mail', 'postUrl').strip()

def getCycle():
    return int(parser.get('global', 'cycle').strip())

if __name__ == '__main__':
    print os.getcwd().split('MQMonitor')[0] + 'MQMonitor/conf/env.ini'