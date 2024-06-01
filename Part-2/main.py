from device import Device
from ethernet import Ethernet
from serialcom import SerialDriver

def main():
    #Example for Ethernet
    ethernet_driver=Ethernet("192.168.1.100",8080)
    ethernet_device=Device(ethernet_driver)
    
    quick_test=ethernet_device.quick_test()
    print(f"Ethernet Quick Test Result : {'Pass' if quick_test else 'Fail'}")
    
    full_test=ethernet_device.full_test()
    print(f"Ethernet Full Test Result : {'Pass' if full_test else 'Fail'}")
    
    #Example for Serial Com.
    serial_driver=SerialDriver("COM3",8080,"RS-485") # For GNU/Linux -> /dev/ttyUSB0
    serial_device=Device(serial_driver)
    
    quick_test=serial_device.quick_test()
    print(f"Serial Device Quick Test Result : {'Pass' if quick_test else 'Fail'}")
    
    full_test=serial_device.full_test()
    print(f"Serial Device Full Test Result : {'Pass' if full_test else 'Fail'}")

if __name__=="__main__":
    main()