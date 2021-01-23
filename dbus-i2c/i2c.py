#!/usr/bin/python

# Thie file can be extended to add class drivers for additional devices as they are implemented and tested
# https://github.com/Gozem/am2320/blob/master/am2320.py
# file has been updated to catch and report errors (rather than raising and exception
# use i2cdetect -y 1 on venus Rpi to check the device is found at address 5c

import posix
from fcntl import ioctl
import time

class AM2320:
  I2C_ADDR = 0x5c
  I2C_SLAVE = 0x0703 

  def __init__(self, i2cbus = 1):
    self._i2cbus = i2cbus

  @staticmethod
  def _calc_crc16(data):
    crc = 0xFFFF
    for x in data:
      crc = crc ^ x
      for bit in range(0, 8):
        if (crc & 0x0001) == 0x0001:
          crc >>= 1
          crc ^= 0xA001
        else:
          crc >>= 1
    return crc

  @staticmethod
  def _combine_bytes(msb, lsb):
    return msb << 8 | lsb


  def readSensor(self):
    fd = posix.open("/dev/i2c-%d" % self._i2cbus, posix.O_RDWR)

    ioctl(fd, self.I2C_SLAVE, self.I2C_ADDR)
  
    # wake AM2320 up, goes to sleep to not warm up and affect the humidity sensor 
    # This write will fail as AM2320 won't ACK this write
    try:
      posix.write(fd, b'\0x00')
    except:
      pass
    time.sleep(0.001)  #Wait at least 0.8ms, at most 3ms
  
    # write at addr 0x03, start reg = 0x00, num regs = 0x04 */  
    try:
      posix.write(fd, b'\x03\x00\x04')
    except:
      posix.close(fd)
      return (0,0,1,"Device did not acknowledge request")
    time.sleep(0.0016) #Wait at least 1.5ms for result

    # Read out 8 bytes of result data
    # Byte 0: Should be Modbus function code 0x03
    # Byte 1: Should be number of registers to read (0x04)
    # Byte 2: Humidity msb
    # Byte 3: Humidity lsb
    # Byte 4: Temperature msb
    # Byte 5: Temperature lsb
    # Byte 6: CRC lsb byte
    # Byte 7: CRC msb byte
    data = bytearray(posix.read(fd, 8))
    posix.close(fd)

    # Check data[0] and data[1]
    if data[0] != 0x03 or data[1] != 0x04:
      return (0,0,4,"First two read bytes are a mismatch")
    # raise Exception("First two read bytes are a mismatch")

    # CRC check
    if self._calc_crc16(data[0:6]) != self._combine_bytes(data[7], data[6]):
      return (0,0,4,"CRC failed")
    #  raise Exception("CRC failed")
    
    # Temperature resolution is 16Bit, 
    # temperature highest bit (Bit15) is equal to 1 indicates a
    # negative temperature, the temperature highest bit (Bit15)
    # is equal to 0 indicates a positive temperature; 
    # temperature in addition to the most significant bit (Bit14 ~ Bit0)
    # indicates the temperature sensor string value.
    # Temperature sensor value is a string of 10 times the
    # actual temperature value.
    temp = self._combine_bytes(data[4], data[5])
    if temp & 0x8000:
      temp = -(temp & 0x7FFF)
    temp /= 10.0
  
    humi = self._combine_bytes(data[2], data[3]) / 10.0

    return (temp, humi, 0,'')  

#am2320 = AM2320(1)
#(t,h) = am2320.readSensor()
#print 'temperature', t
#print 'humidiy', h, ' %'
