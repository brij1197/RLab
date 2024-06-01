from constants import BUFFERSIZE
from driver import Driver

from serial import Serial,SerialException

class SerialDriver(Driver):
    def __init__(self, port, baudrate, protocol):
        self.port = port
        self.baudrate = baudrate
        self.protocol = protocol
        self.ser = None
    
    def connect(self) -> bool:
        try:
            self.ser = Serial(self.port, self.baudrate)
            if not self.ser.is_open:
                self.ser.open()
            return True
        except SerialException as e:
            print(f"Serial connection error: {e}")
            return False
    
    def disconnect(self) -> bool:
        if self.ser and self.ser.is_open:
            self.ser.close()
            self.ser = None
            return True
        return False
    
    def send(self, command: str) -> bool:
        try:
            self.ser.write(command.encode())
            return True
        except SerialException as e:
            print(f"Serial send error: {e}")
            return False
    
    def receive(self) -> str:
        try:
            return self.ser.read(BUFFERSIZE).decode()
        except SerialException as e:
            print(f"Serial receive error: {e}")
            return None
