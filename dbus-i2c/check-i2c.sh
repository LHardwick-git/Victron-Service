#! /bin/sh

if ! pgrep -f "dbus-i2c.py" >/dev/null; then
    echo "process not found"
  else
    echo "process running"
  fi
