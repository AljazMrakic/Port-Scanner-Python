import socket
import subprocess
import sys
import os
from datetime import datetime

# import pyfiglet module for stylised text
import pyfiglet

os.system("cls")

green = "\033[1;32m"

title = pyfiglet.figlet_format("PORTSCAN", font = "slant")
print(green, title) # prints the name of the tool

hostname = socket.gethostname() # gets the name of the computer
ipaddr = socket.gethostbyname(hostname) # gets the ip of the computer(hostname)

# MAIN FUNCTION
def main():
    chooseService()

# function for choosing a service
def chooseService():
    ansServ = input("Services: \n\ni    - get your ip \ns    - scan specified ip \nexit - exit scanner\n") #choose a service
    
    if ansServ == "i": # get ip
        get_local_ip()
    elif ansServ == "s": # scan ip
        get_parameter_for_scan()
    elif ansServ == "exit":
        sys.exit() # exit service
    else:
        print("\nERROR: Service does not exist!") #if the service doesn't exist
    
# function for getting your personal ip and computer name
def get_local_ip():
    ansIp = input("\nDo you want to know your IP address? (y/n) : ")

    if ansIp == "y":
        print("\nYour computer name is : ", hostname)
        print("Here is your IP : ", ipaddr)
        print("="*45)
        chooseService()
    elif ansIp == "n":
        chooseService()
    else:
        print("WRONG INPUT. Use 'y' or 'n'.")

# function for setting scanning parameters for a port scan on a specific ip
def get_parameter_for_scan():
    subprocess.call("", shell=True)
    iptoscan = input("\nEnter an ip you wish to scan : ") #ip to scan
    ansSc = input("Do you wish to scan all ports (y/n) : ")

    if ansSc == "y":
        port1 = 0
        port2 = 49151
        scanning_ip(port1, port2, iptoscan)
    elif ansSc == "n":
        port1 = int(input("Enter start port number : "))
        port2 = int(input("Enter last port number : "))
        scanning_ip(port1, port2, iptoscan)
    else:
        print("WRONG INPUT. Use 'y' or 'n'.")

# function to start a scan
def scanning_ip(port1, port2, iptoscan):
    timeStart = datetime.now()
    print("\nSCANNING STARTED...")

    try:
        for port in range(port1, port2): # loop through the numbers from port1 to port2
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            response = soc.connect_ex((iptoscan, port))
            if response == 0:
                print("PORT OPEN : ", port)
            soc.close()
    except KeyboardInterrupt: # cancel scan with keyboard
        print("\nSCANNING CANCELED!")
        sys.exit()
    except Exception as e:
        print(e)
        sys.exit()
    
    timeFinish = datetime.now()
    timeScan = timeFinish - timeStart
    print("\nSCANNING SUCCESSFUL! TIME: ", timeScan)
    print("="*45)
    chooseService()
   
if __name__ == "__main__":
    main()
    
		




