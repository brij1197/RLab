from driver import Driver

class Device:
    def __init__(self,driver:Driver):
        self.driver=driver
    
    def initialize(self):
        self.driver.connect()
    
    def shutdown(self):
        self.driver.disconnect()
    
    def transmit(self,command:str):
        self.driver.send(command)
    
    def response(self) -> str:
        return self.driver.receive()
    
    def quick_test(self) -> bool:
        self.initialize()
        self.transmit("QUICK")
        response=self.response()
        self.shutdown()
        return response=="QUICK"
    
    def full_test(self) -> bool:
        self.initialize()
        self.transmit("FULL")
        response=self.response()
        self.shutdown()
        return response=="FULL"