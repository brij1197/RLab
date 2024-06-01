from device import Device
from ethernet import Ethernet
from serialcom import SerialDriver

class DeviceSelection:
    def __init__(self) -> None:
        self.__device = None
        
    def ethernetdriver(self, ip, port):
        ethernet_driver = Ethernet(ip, port)
        self.__device = Device(ethernet_driver)
    
    def serialdriver(self, port, baudrate, protocol):
        serial_driver = SerialDriver(port, baudrate, protocol)
        self.__device = Device(serial_driver)
    
    def quicktest(self):
        try:
            quick_test = self.__device.quick_test()
            print(f"Device Quick Test Result: {'Pass' if quick_test else 'Fail'}")
        except Exception as e:
            print(f"Quick test failed: {e}")
        
    def fulltest(self):
        try:
            full_test = self.__device.full_test()
            print(f"Device Full Test Result: {'Pass' if full_test else 'Fail'}")
        except Exception as e:
            print(f"Full test failed: {e}")
