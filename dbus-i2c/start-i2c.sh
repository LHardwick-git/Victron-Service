#! /bin/sh

if [ ! -e /dev/i2c-* ]; then
    svc -d /service/dbus-i2c
    exit
fi
     
    exec $(dirname $0)/dbus-i2c.py

