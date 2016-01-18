# RabbitMQ监控平台

## 功能

提供web界面订阅队列，后台线程定时轮询队列堆积数量，通过邮件的方式告警。

## 环境依赖

1. python2
1. mongo
1. flask

## 使用说明

1. 配置conf/env.ini

  ```
  [global]
  ; 全局配置，对所有队列统一指定消息堆积阀值和接警人
  msgTotalMax=10000000
  mailList=liyanhong@baidu.com
  ; 忽略某些队列
  ignoreQueueList=abc,cde
  ; 后台线程监控周期，以秒为单位
  cycle=120
  
  [mq]
  ; mq地址、用户名、密码
  addr=58.215.141.110:15672
  username=test
  password=test
  
  [mongo]
  ; 监控数据采用mongo存储
  host=localhost
  port=27017
  
  [mail]
  ; 邮件配置
  fromAddr=notonly@163.com
  password=uwofigy
  smtpServer=smtp.163.com
  smtpPort=25
  ```
1. 运行脚本：sh control.sh start/stop/restart/status
1. 访问localhost:5000订阅队列。

