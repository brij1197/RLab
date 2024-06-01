from driver import Driver
import serial

class SerialDriver(Driver):
    
    def __init__(self, port, baudrate,protocol):
        self.port=port
        self.baudrate=baudrate
        self.protocol=protocol#enum
        self.ser=None
    
    def connect(self):
        self.ser=serial.Serial(self.port,self.baudrate)
        if not self.ser.is_open:
            self.ser.open()
    
    def disconnect(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            self.ser=None
    
    def send(self,command:str):
        self.ser.write(command.encode())
        
    def receive(self) -> str:
        return self.ser.read(1024).decode()