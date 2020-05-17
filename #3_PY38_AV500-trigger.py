# -*- conding: utf-8 -*-

import socket
import time
#set phase time (s)
phaseTime = 2

# address and port is arbitrary
def client(host="10.0.40.20", port=51237):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))

    while True:

        
        #print("[+] Received", repr(response.decode('utf-8')))
        key = input("<t>-phase on, <r>-read data\n")
        if key == "t":
            tmsg = 'S'
            print("[+] Sending to {}:{}".format(host, port))
            sock.sendall(tmsg.encode('utf-8'))
            print("Trigger sent")
            time.sleep(phaseTime)
            tmsg = 'E'
            print("[+] Sending to {}:{}".format(host, port))
            sock.sendall(tmsg.encode('utf-8'))
            print("Trigger stop")            
        if key == "r":
            response = sock.recv(4096)
            
            if not response:
                print("[-] Not Received")
                

      

if __name__ == "__main__":
  client()
  
