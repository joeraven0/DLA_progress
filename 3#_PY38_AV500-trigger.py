# -*- conding: utf-8 -*-

import socket
import keyboard

# address and port is arbitrary
def client(host="10.0.40.20", port=51237):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))

    while True:
          #data = input("[+] Enter string : ")
          #sock.sendall(data.encode('utf-8'))
          #print("[+] Sending to {}:{}".format(host, port))
        #print("[+] Received", repr(response.decode('utf-8')))
        if keyboard.read_key() == "t":
            tmsg = 'S'
            sock.sendall(tmsg.encode('utf-8'))
            print("Trigger sent")
        if keyboard.read_key() == "s":
            tmsg = 'E'
            sock.sendall(tmsg.encode('utf-8'))
            print("Trigger stop")
        if keyboard.read_key() == "r":
            response = sock.recv(4096)
        
            if not response:
                print("[-] Not Received")
                

      

if __name__ == "__main__":
  print("<t>-phase on, <s>-phase off, <r>-read data")
  client()
  
