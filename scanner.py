from socket import * 
ip = input("Enter the ip address: ")
port_start = int(input("Enter the port to start the scan from : "))
port_stop = int(input("Enter the port to stop the scan the scan on: "))
main_array = []
for port in range(port_start,port_stop+1):
    addr = (ip, port)
    s = socket(AF_INET,SOCK_STREAM)
    result = s.connect_ex(addr)
    setdefaulttimeout(0.01)
    s.close()
    if (result == 0):
        print("The port number {} is open".format(port))
        main_array.append(port)
    else:
        print("The port number {} is not open".format(port))
print("-"*40)
print("The scanning is done...")
print("The ports which are open are: ")
print(main_array)
