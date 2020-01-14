import socket
import threading

class ServerThread:
    def __init__(self,soc):
        self.soc = soc
    
    def doCommunicate(self):
        print("Threading started")
        msg = ' '
        while msg !='q':
            print("Receiving message")            
            msg = self.soc.recv(1024).decode("utf-8")            
            print("Client -> ",msg)
            sms = input('enter the Message to client: ')
            self.soc.send(sms.encode('utf-8'))
        self.soc.close()


server = socket.socket()

server.bind(('localhost', 3690))

server.listen(5)

while True:
    print("Waiting for client")
    soc, addr = server.accept()
    print("Client connected with address ",addr)    
    serverThread = ServerThread(soc)
    t1 = threading.Thread(target = serverThread.doCommunicate)
    t1.start()



