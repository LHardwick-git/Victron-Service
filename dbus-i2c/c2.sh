#! /bin/sh

if [ ! -e /dev/i2c-* ]; then
    svc -d /service/dbus-i2c
    exit
else
   echo "device driver found"
fi

