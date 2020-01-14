import socket

soc = socket.socket()
soc.connect(('localhost', 3690))

msg = ''
while msg != 'q':
    msg = input("Enter the message: ")
    soc.send(msg.encode('utf-8'))
    rply = soc.recv(1024).decode('utf-8')
    print("Server -> ", rply)
soc.close()
