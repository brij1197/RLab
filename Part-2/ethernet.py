from driver import Driver
import socket

class Ethernet(Driver):
    
    def __init__(self,ip,port):
        self.ip=ip
        self.port=port
        self.sock=None
    
    def connect(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((self.ip,self.port))
    
    def disconnect(self):
        if self.sock:
            self.sock.close()
            self.sock=None
            
    def send(self,command:str):
        self.sock.sendall(command.encode())
    
    def receive(self) -> str:
        return self.sock.recv(1024).decode()
    