#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Sep 23, 2015

@author: mountain
'''
from app import web
from flask import render_template
from flask import request
from app.service import MQService
from app.util import ConfUtil
import json
from app.util.LogUtil import log

@web.route('/mq',methods = ['GET'])
@web.route('/',methods = ['GET'])
def index():
    try:
        addrList = ConfUtil.getMQAddrList()
        addr = request.args.get('addr', addrList[0])
        queues = MQService.getQueues(addr)
        addrList.remove(addr)
        addrList.insert(0, addr)
    except Exception, e:
        log.error(e)
    return render_template("mq/index.html", addrList = addrList, queues = queues)

@web.route('/mq/sub', methods = ['POST'])
def subQueue():
    data = json.loads(request.data)
    MQService.subQueue(data)
    res = {}
    res['msg'] = 'ok'
    return json.dumps(res)
