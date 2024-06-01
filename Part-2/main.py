from deviceselection import DeviceSelection

device=DeviceSelection()

def ethernetconfig() -> None:
    print("Enter the following: ")
    print("IP:")
    ip=str(input())
    print("Port:")
    port=int(input())
    ethernetconfig(ip,port)
    device.ethernetdriver(ip,port)
    print("Do you want to run a Quick Test (Y/N): ")
    option=input()
    if(option.lower()=='y'):
        device.quicktest()
    print("Do you want to run a Full Test (Y/N): ")
    option=input()
    if(option.lower()=='y'):
        device.fulltest()


def main():
    quit=False
    print("---------Device Type---------")
    print("1. Ethernet")
    print("2. Serial")
    print("3. Exit")
    
    print(" Enter Choice: ")
    
    while not quit:
        choice=int(input())
        match choice:
            case 1:
                ethernetconfig()
            case 2:
                pass
            case 3:
                quit()
            
if __name__=="__main__":
    main()