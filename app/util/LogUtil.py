#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Sep 28, 2015

@author: mountain
'''
import logging

log = logging.getLogger('monitor')
log.setLevel(logging.INFO)
fh = logging.FileHandler('monitor.log')
fh.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s %(filename)s %(lineno)s %(levelname)s [%(message)s]", "%Y-%m-%d %H:%M:%S")
fh.setFormatter(formatter)
log.addHandler(fh)

def error(msg):
    log.error(msg)

def info(msg):
    log.info(msg)

if __name__ == '__main__':
    log.info('haha')