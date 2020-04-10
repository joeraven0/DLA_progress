import serial
import time
import codecs
import sys

ser = serial.Serial("COM7",baudrate=9600)



def sendcmd(msg):
    x=10

    if (msg == '$S')or(msg=='$s'):
        msg += '\r'
        print('$ found: ',msg)
    msg = bytes(msg,encoding='utf-8')
    ser.write(msg)
    print('Sent: ', str(msg,'utf-8'))
    time.sleep(.1)
    nackmsg = receivemsg()


    try:
        print('Received: ', str(nackmsg,'utf-8'))
    except:
        print("Exception")
    if str(nackmsg,'utf-8')=='>':
        print('Command successfully sent!')

def receivemsg():
    return ser.read()


sendcmd('$S')

sendcmd('$CBPVO01')

sendcmd('$s')
input('Key to close com port')
ser.close()
