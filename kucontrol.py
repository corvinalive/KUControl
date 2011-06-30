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
import serial, struct, binascii, time, sys
from PySide import QtCore, QtGui
from upvaui import Ui_MainWindow

class MyMainWindow(QtGui.QMainWindow):
    
    def pushButtonf1(self):
        f=self.ui.doubleSpinBoxf1.value()
        s=":WF1"+str(f)+'\15'
        self.ser.write(s)

    def pushButtonf2(self):
        f=self.ui.doubleSpinBoxf2.value()
        s=":WF2"+str(f)+'\15'
        self.ser.write(s)

    def pushButtonf3(self):
        f=self.ui.doubleSpinBoxf3.value()
        s=":WF3"+str(f)+'\15'
        self.ser.write(s)

    def pushButtonf4(self):
        f=self.ui.doubleSpinBoxf4.value()
        s=":WF4"+str(f)+'\15'
        self.ser.write(s)

    def pushButtont1(self):
        f=self.ui.doubleSpinBoxf1.value()
        s=":WT1"+str(f)+'\15'
        self.ser.write(s)

    def pushButtont2(self):
        f=self.ui.doubleSpinBoxf2.value()
        s=":WT2"+str(f)+'\15'
        self.ser.write(s)

    def pushButtont3(self):
        f=self.ui.doubleSpinBoxf3.value()
        s=":WT3"+str(f)+'\15'
        self.ser.write(s)

    def pushButtont4(self):
        f=self.ui.doubleSpinBoxf4.value()
        s=":WT4"+str(f)+'\15'
        self.ser.write(s)



    def pushButtonn(self):
        f=self.ui.spinBoxn.value()
        s=":WN"+str(f)+'\15'
        self.ser.write(s)

    def pushButtonsa(self):
        s=":SA"'\15'
        self.ser.write(s) 
    def pushButtonsb(self):
        s=":SB"'\15'
        self.ser.write(s)         
         
    def pushButtona1(self):
        f=self.ui.A1box.value()
        s=":WA1"+str(f)+'\15'
        self.ser.write(s)

    def pushButtona2(self):
        f=self.ui.A2box.value()
        s=":WA2"+str(f)+'\15'
        self.ser.write(s)
        
    def pushButtona3(self):
        f=self.ui.A3box.value()
        s=":WA3"+str(f)+'\15'
        self.ser.write(s)
        
    def pushButtona3(self):
        f=self.ui.A3box.value()
        s=":WA3"+str(f)+'\15'
        self.ser.write(s)
        
    def pushButtona4(self):
        f=self.ui.A4box.value()
        s=":WA4"+str(f)+'\15'
        self.ser.write(s)
        
    def pushButtona5(self):
        f=self.ui.A5box.value()
        s=":WA5"+str(f)+'\15'
        self.ser.write(s)
        
    def pushButtona6(self):
        f=self.ui.A6box.value()
        s=":WA6"+str(f)+'\15'
        self.ser.write(s)
        
    def pushButtona7(self):
        f=self.ui.A7box.value()
        s=":WA7"+str(f)+'\15'
        self.ser.write(s)

    def pushButtona8(self):
        f=self.ui.A8box.value()
        s=":WA8"+str(f)+'\15'
        self.ser.write(s)

    def pushButtonset4(self):
        delay=0.5
        for i in range(8):
            s=":WA"+str(i+1)+"4"'\15'
            print s,"\n"
            self.ser.write(s)
            time.sleep(delay)
            
    def pushButtonset12(self):
        delay=0.5
        for i in range(8):
            s=":WA"+str(i+1)+"12"'\15'
            print s,"\n"
            self.ser.write(s)
            time.sleep(delay)
            
    def pushButtonset20(self):
        delay=0.5
        for i in range(8):
            s=":WA"+str(i+1)+"20"'\15'
            print s,"\n"
            self.ser.write(s)
            time.sleep(delay)                        

    def pushButtonreadall(self):
        delay=0.5
        #читаем аналоговые входа
        s=":GA1"'\15'
        self.ser.write(s)
        y=self.ser.read(20)
        self.ui.label1.setText(y[1:])
        time.sleep(delay)
        
        s=":GA2"'\15'
        self.ser.write(s)
        y=self.ser.read(20)
        self.ui.label2.setText(y[1:])
        time.sleep(delay)

        s=":GA3"'\15'
        self.ser.write(s)
        y=self.ser.read(20)
        self.ui.label3.setText(y[1:])
        time.sleep(delay)

        s=":GA4"'\15'
        self.ser.write(s)
        y=self.ser.read(20)
        self.ui.label4.setText(y[1:])
        time.sleep(delay)

        s=":GA5"'\15'
        self.ser.write(s)
        y=self.ser.read(20)
        self.ui.label5.setText(y[1:])
        time.sleep(delay)

        s=":GA6"'\15'
        self.ser.write(s)
        y=self.ser.read(20)
        self.ui.label6.setText(y[1:])
        time.sleep(delay)

        s=":GA7"'\15'
        self.ser.write(s)
        y=self.ser.read(20)
        self.ui.label7.setText(y[1:])
        time.sleep(delay)

        s=":GA8"'\15'
        self.ser.write(s)
        y=self.ser.read(20)
        self.ui.label8.setText(y[1:])
        time.sleep(delay)

		#Читаем частотные входа
		# 1
        s=":GF1"'\15'
        self.ser.write(s)
        y=self.ser.read(20)
        fnt=u" "+y[1:]+" Hz \n"
        time.sleep(delay)
        s=":GT1"'\15'
        self.ser.write(s)
        y=self.ser.read(20)
        fnt+=y[1:]+" mks"        
        self.ui.labelf1.setText(fnt)
        time.sleep(delay)
        # 2
        s=":GF2"'\15'
        self.ser.write(s)
        y=self.ser.read(20)
        fnt=u" "+y[1:]+" Hz \n"
        time.sleep(delay)
        s=":GT2"'\15'
        self.ser.write(s)
        y=self.ser.read(20)
        fnt+=y[1:]+" mks"        
        self.ui.labelf2.setText(fnt)
        time.sleep(delay)
		#3
        s=":GF3"'\15'
        self.ser.write(s)
        y=self.ser.read(20)
        fnt=u" "+y[1:]+" Hz \n"
        time.sleep(delay)
        s=":GT3"'\15'
        self.ser.write(s)
        y=self.ser.read(20)
        fnt+=y[1:]+" mks"        
        self.ui.labelf3.setText(fnt)
        time.sleep(delay)
        #4
        s=":GF4"'\15'
        self.ser.write(s)
        y=self.ser.read(20)
        fnt=u" "+y[1:]+" Hz \n"
        time.sleep(delay)
        s=":GT4"'\15'
        self.ser.write(s)
        y=self.ser.read(20)
        fnt+=y[1:]+" mks"        
        self.ui.labelf4.setText(fnt)
        
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=0.5)#,rtscts=0)
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.parity = serial.PARITY_NONE
        self.ser.setDTR(1)
        self.ser.setRTS(0)
        self.connect(self.ui.pushButtonf1, QtCore.SIGNAL("clicked()"), self.pushButtonf1)
        self.connect(self.ui.pushButtonf2, QtCore.SIGNAL("clicked()"), self.pushButtonf2)
        self.connect(self.ui.pushButtonf3, QtCore.SIGNAL("clicked()"), self.pushButtonf3)
        self.connect(self.ui.pushButtonf4, QtCore.SIGNAL("clicked()"), self.pushButtonf4)
        self.connect(self.ui.pushButtonn, QtCore.SIGNAL("clicked()"), self.pushButtonn)
        self.connect(self.ui.pushButtonsa, QtCore.SIGNAL("clicked()"), self.pushButtonsa)        
        self.connect(self.ui.pushButtonsb, QtCore.SIGNAL("clicked()"), self.pushButtonsb)
        self.connect(self.ui.A1pushButton, QtCore.SIGNAL("clicked()"), self.pushButtona1)
        self.connect(self.ui.A2pushButton, QtCore.SIGNAL("clicked()"), self.pushButtona2)
        self.connect(self.ui.A3pushButton, QtCore.SIGNAL("clicked()"), self.pushButtona3)
        self.connect(self.ui.A4pushButton, QtCore.SIGNAL("clicked()"), self.pushButtona4)
        self.connect(self.ui.A5pushButton, QtCore.SIGNAL("clicked()"), self.pushButtona5)
        self.connect(self.ui.A6pushButton, QtCore.SIGNAL("clicked()"), self.pushButtona6)
        self.connect(self.ui.A7pushButton, QtCore.SIGNAL("clicked()"), self.pushButtona7)
        self.connect(self.ui.A8pushButton, QtCore.SIGNAL("clicked()"), self.pushButtona8)
        self.connect(self.ui.set4pushButton, QtCore.SIGNAL("clicked()"), self.pushButtonset4)
        self.connect(self.ui.set12pushButton, QtCore.SIGNAL("clicked()"), self.pushButtonset12)
        self.connect(self.ui.set20pushButton, QtCore.SIGNAL("clicked()"), self.pushButtonset20)
        self.connect(self.ui.pushButtont1, QtCore.SIGNAL("clicked()"), self.pushButtont1)
        self.connect(self.ui.pushButtont2, QtCore.SIGNAL("clicked()"), self.pushButtont2)
        self.connect(self.ui.pushButtont3, QtCore.SIGNAL("clicked()"), self.pushButtont3)
        self.connect(self.ui.pushButtont4, QtCore.SIGNAL("clicked()"), self.pushButtont4)
        self.connect(self.ui.pushButtonreadall, QtCore.SIGNAL("clicked()"), self.pushButtonreadall)
		
    

def main():

    
	#Open the com port

    #ser.setCTS(0)
    #s=":WF11000"'\15'
    #s=":GT3"'\15'
    #s='\1''\3''\14''\32''\0''\1''\246''\235'
    #print s
    #x = struct.pack('8s',":WF1700"'\15')
    #print x, 'newline',binascii.hexlify(x) # 02   ID,0x03,0x01,0x2,0x03,0x04
    #ser.write(s)
    #time.sleep(1)
    #s=":GF1"'\15'
    #ser.setDTR('1')
    #print s,'\n' 'newline',binascii.hexlify(s) # 02
    #ser.write(s)
    #time.sleep(0.5)
    
    #y = ser.readline()
    #print "y=",y,len(y),"\ny=",binascii.hexlify(y)
   
   
    app = QtGui.QApplication(sys.argv)
    myapp = MyMainWindow()
    myapp.show()
    result=app.exec_()
    myapp.ser.close()
    sys.exit(result)
    
    #ser.write(x.encode("Latin1"))
    #x = ser.read()          # read one byte
    #s = ser.read(10)        # read up to ten bytes (timeout)
    #print s
    #line = ser.readline()   # read a '\n' terminated line

    return 0

if __name__ == '__main__':
	main()

