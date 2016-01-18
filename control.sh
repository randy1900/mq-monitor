#! /bin/sh
DAEMON='python start.py'
NAME=mq-monitor
PIDFILE=$NAME.pid

start() {
    if [ -f $PIDFILE ]
    then
        if [ -n "$(ps aux | grep $(cat $PIDFILE) | grep $DAEMON)" ]
        then
            echo "$NAME is running."
            exit 0
        else
            rm -f $PIDFILE
        fi
    fi
    echo "Starting $NAME."
    $DAEMON > /dev/null 2>&1 & 
    echo $! > $PIDFILE
}

stop() {
    if [ ! -f $PIDFILE ]
    then
        echo "$NAME is not running."
        exit 0
    fi
    if [ -z "$(ps aux | grep $(cat $PIDFILE) | grep $DAEMON)" ]
    then
        echo "$NAME is not running."
        rm -f $PIDFILE
        exit 0
    fi
    echo "Stopping $NAME."
    pid=$(cat $PIDFILE)    
    kill $pid
    rm -f $PIDFILE
}

restart() {
    if [ -f $PIDFILE ]
    then
        echo "Stopping $NAME."
        if [ -n "$(ps aux | grep $(cat $PIDFILE) | grep $DAEMON)" ]
        then
            kill $(cat $PIDFILE)
        fi
        rm -f $PIDFILE
    fi
    start
}

status() {
    if [ ! -f $PIDFILE ]
    then
        echo "$NAME is not running."
        exit 0
    fi
    if [ -n "$(ps aux | grep $(cat $PIDFILE) | grep $DAEMON)" ]
    then
        echo "$NAME is running."
    else
        echo "$NAME is not running."
    fi
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        restart
        ;;
    status)
        status
        ;;
    *)
        echo "Usage: sh $control.sh start/stop/restart/status"
esac
exit 0
