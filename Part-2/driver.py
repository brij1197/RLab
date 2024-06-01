from abc import ABC, abstractmethod

class Driver(ABC):
    @abstractmethod
    def connect(self) -> bool:
        pass
    
    @abstractmethod
    def disconnect(self) -> bool:
        pass
    
    @abstractmethod
    def send(self, command: str) -> bool:
        pass
    
    @abstractmethod
    def receive(self) -> str:
        pass
