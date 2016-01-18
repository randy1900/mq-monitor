#!/usr/bin/python
# -*- coding: utf-8 -*-
from app import web
from app.monitor.Monitor import Monitor
import threading, time
from app.util import ConfUtil
from app.util.LogUtil import log

def run():
    monitor = Monitor()
    while True:
        try:
            monitor.check()
        except Exception, e:
            log.error(e)
        time.sleep(ConfUtil.getCycle())

if __name__ == '__main__':
    thread = threading.Thread(target = run, name = 'monitor')
    thread.start()
    log.info('Starting...')
    web.run(host='0.0.0.0', port=5000)