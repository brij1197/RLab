from deviceselection import DeviceSelection
from constants import SERIALPORT, PROTOCOL

device = DeviceSelection()

def ethernetconfig() -> None:
    try:
        ip = input("Enter IP: ")
        port = int(input("Enter Port: "))
        device.ethernetdriver(ip, port)
        option = input("Do you want to run a Quick Test (Y/N): ").lower()
        if option == 'y':
            device.quicktest()
        option = input("Do you want to run a Full Test (Y/N): ").lower()
        if option == 'y':
            device.fulltest()
    except ValueError as e:
        print(f"Invalid input: {e}")
        
def serialconfig() -> None:
    try:
        port = input("Enter Port: ")
        if port not in SERIALPORT._member_names_:
            raise ValueError(f"Invalid port. Allowed values: {', '.join(SERIALPORT._member_names_)}")
        
        baudrate = int(input("Enter Baudrate: "))
        
        protocol = input("Enter Protocol: ")
        if protocol not in PROTOCOL._member_names_:
            raise ValueError(f"Invalid protocol. Allowed values: {', '.join(PROTOCOL._member_names_)}")
        
        device.serialdriver(port, baudrate, protocol)
        option = input("Do you want to run a Quick Test (Y/N): ").lower()
        if option == 'y':
            device.quicktest()
        option = input("Do you want to run a Full Test (Y/N): ").lower()
        if option == 'y':
            device.fulltest()
    except ValueError as e:
        print(f"Invalid input: {e}")

def main():
    quit = False
    while not quit:
        try:
            print("---------Device Type---------")
            print("1. Ethernet")
            print("2. Serial")
            print("3. Exit")
            choice = int(input("Enter Choice: "))
            match choice:
                case 1:
                    ethernetconfig()
                case 2:
                    serialconfig()
                case 3:
                    quit = True
                case _:
                    print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
