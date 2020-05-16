from LogCollector.grabber import start_monitor
from time import sleep
from threading import Thread
from SmartContract.read import read
from SmartContract.write import write
from os import system, path, _exit
from queue import Queue
import sys
from datetime import datetime

def pre_menu():
    print("1) Connect as a Client.")
    print("2) Start a server.")

    inp = int(input())
    ip_addr = ""
    if inp == 1:
        ip_addr = input('Enter IP address of Master Server:')
    else:
        print('Start Ganache on 0.0.0.0 and hit enter.')
        ip_addr = "0.0.0.0"
    
    address = print("Enter Address of Smart Contract") 
    return "http://" + ip_addr + ":" + "7545" , address, inp

def menu_client():
    print("1) Fetch Updates From Blockchain and Apply.")
    print("2) Exit.")

    inp = int(input())
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    
    if inp == 1:
        read(ganache_url, path_to_abi, address, server_id, datetime.fromtimestamp(timestamp))
    else:
        exit(0)

def menu_server():
    print("1) Run Command")
    print("2) Install Package")
    print("3) Update System")
    
    inp = int(input())
    typ = inp
    data = ""

    if inp == 1:
        data = input("Enter Command to run")
    elif inp == 2:
        data = input("Enter package name to install") 
    elif inp == 3:
        data = "apt-get update && apt-get upgrade"
    
    print("Writing data to Blockchain")
    write(ganache_url, path_to_abi, address, server_id, [typ, data])
    print("Write Successful!")

print("Welcome to Update Utility")
ganache_url, address, inp = pre_menu()

started = False
path_to_abi = path.abspath('abi.json')
#address = "0x490E92418a235eA728A6d11541b185F850929B9f"
server_id = 3333

if inp == 1:
    menu_client()
else:
    menu_server()



