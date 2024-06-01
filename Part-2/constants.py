from enum import Enum

SERIALPORT = Enum('SERIALPORT', ['COM3', '/dev/ttyUSB0'])
PROTOCOL = Enum('PROTOCOL', ['RS-422', 'RS-485'])
BUFFERSIZE = 1024
