from constants import BUFFERSIZE
from driver import Driver

from socket import socket,AF_INET,SOCK_STREAM,error

class Ethernet(Driver):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = None
    
    def connect(self) -> bool:
        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect((self.ip, self.port))
            return True
        except error as e:
            print(f"Ethernet connection error: {e}")
            return False
    
    def disconnect(self) -> bool:
        if self.sock:
            self.sock.close()
            self.sock = None
            return True
        return False
    
    def send(self, command: str) -> bool:
        try:
            self.sock.sendall(command.encode())
            return True
        except error as e:
            print(f"Ethernet send error: {e}")
            return False
    
    def receive(self) -> str:
        try:
            return self.sock.recv(BUFFERSIZE).decode()
        except error as e:
            print(f"Ethernet receive error: {e}")
            return None
