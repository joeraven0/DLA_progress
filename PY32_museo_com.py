import serial
import time
import codecs
import sys

ser = serial.Serial("COM7",baudrate=115200)



def sendcmd(msg):
    msgBuffer = msg
    msg = bytes(msg,encoding='utf-8')   #Convert command to byte
    ser.write(msg)                      #Write to serial com
    #print('Sent: ', str(msg,'utf-8'))
    time.sleep(.3)                      #Time delay to transmit data
    if msgBuffer!="$Ar\r":              #For all commands except for end hmp
        try:
            nackmsg = receivemsg()
            print('Received: ', str(nackmsg,'utf-8'))
        except:
            print("Exception")
        if str(nackmsg,'utf-8')=='$>':
            print('Command successfully sent!')

def receivemsg():                       #Read com data
    whilecnt = 0                        #To avoid infinite loop
    while whilecnt<10:
        whilecnt +=1
        if ser.in_waiting > 0:
            receivedfun = ser.read(ser.in_waiting)
            return receivedfun


sendcmd('$S\r')
sendcmd('$-$!\r')
sendcmd('$CSNRM04\r$CBPVO00\r')
sendcmd('$Ar\r')

input('Press key to close com port...')
ser.close()
