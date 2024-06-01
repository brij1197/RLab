from device import Device
from ethernet import Ethernet
from serialcom import SerialDriver

class DeviceSelection:
    def __init__(self) -> None:
        self.__device=None
        
    def ethernetdriver(self, ip, port):
        ethernet_driver=Ethernet(ip,port)
        self.__device=Device(ethernet_driver)
    
    def serialdriver(self, port, baudrate, protocol):
        serial_driver=SerialDriver(port,baudrate,protocol) # For GNU/Linux -> /dev/ttyUSB0
        self.__device=Device(serial_driver)
    
    def quicktest(self):
        quick_test=self.__device.quick_test()
        print(f"Serial Device Quick Test Result : {'Pass' if quick_test else 'Fail'}")
        
    def fulltest(self):
        full_test=self.__device.full_test()
        print(f"Serial Device Full Test Result : {'Pass' if full_test else 'Fail'}")