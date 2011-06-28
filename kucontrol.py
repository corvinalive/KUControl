#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       kucontrol.py
#       
#       Copyright 2011 Zonov Valerij <corvinalive@yandex.ru>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#       
import serial, struct, binascii, time



def main():
	#ser = serial.Serial(0)  # open first serial port
    #print ser.portstr       # check which port was really used
    #ser.write("hello")      # write a string
    

    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.5,rtscts=0)
    ser.bytesize = serial.EIGHTBITS
    ser.stopbits = serial.STOPBITS_ONE
    ser.parity = serial.PARITY_NONE
    ser.setDTR(1)
    ser.setRTS(0)
    #ser.setCTS(0)
    #s=":WF11000"'\15'
    #s=":GT3"'\15'
    #s='\1''\3''\14''\32''\0''\1''\246''\235'
    #print s
    #x = struct.pack('8s',":WF1700"'\15')
    #print x, 'newline',binascii.hexlify(x) # 02   ID,0x03,0x01,0x2,0x03,0x04
    #ser.write(s)
    time.sleep(1)
    s=":GF1"'\15'
    #ser.setDTR('1')
    print s,'\n' 'newline',binascii.hexlify(s) # 02
    ser.write(s)
    time.sleep(0.5)
    
    y = ser.readline()
    print "y=",y,len(y),"\ny=",binascii.hexlify(y)

    #ser.write(x.encode("Latin1"))
    #x = ser.read()          # read one byte
    #s = ser.read(10)        # read up to ten bytes (timeout)
    #print s
    #line = ser.readline()   # read a '\n' terminated line
    ser.close()
    return 0

if __name__ == '__main__':
	main()

