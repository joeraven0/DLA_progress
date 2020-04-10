import serial
import time
import codecs
import sys

ser = serial.Serial("COM7",baudrate=115200)



def sendcmd(msg):
    msgBuffer = msg
    msg += '\r'
    msg = bytes(msg,encoding='utf-8')
    ser.write(msg)
    print('Sent: ', str(msg,'utf-8'))
    time.sleep(.5)
    if msgBuffer!="$Ar":
        try:
            nackmsg = receivemsg()
            print('Received: ', str(nackmsg,'utf-8'))
        except:
            print("Exception")
        if str(nackmsg,'utf-8')=='$>':
            print('Command successfully sent!')

def receivemsg():
    return ser.read(3)


sendcmd('$S')

sendcmd('$CSNRM00')

sendcmd('$Ar')

#input('Key to close com port')
ser.close()
