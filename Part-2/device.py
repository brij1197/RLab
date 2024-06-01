from driver import Driver

class Device:
    def __init__(self, driver: Driver):
        self.driver = driver
    
    def initialize(self):
        if not self.driver.connect():
            raise ConnectionError("Failed to connect the device.")
    
    def shutdown(self):
        if not self.driver.disconnect():
            raise ConnectionError("Failed to disconnect the device.")
    
    def transmit(self, command: str):
        if not self.driver.send(command):
            raise IOError("Failed to send command.")
    
    def response(self) -> str:
        response = self.driver.receive()
        if response is None:
            raise IOError("Failed to receive response.")
        return response
    
    def quick_test(self) -> bool:
        self.initialize()
        self.transmit("QUICK")
        response = self.response()
        self.shutdown()
        return response == "QUICK"
    
    def full_test(self) -> bool:
        self.initialize()
        self.transmit("FULL")
        response = self.response()
        self.shutdown()
        return response == "FULL"
