import socket
import sys
strHostname = 'google.ch'


target = socket.gethostbyname(strHostname)
print(target)

try: 
    # will scan ports between 1 to 65,535 
    for port in range(79, 81): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        print(f'Checking port {port}')
          
        # returns an error indicator 
        result = s.connect_ex((target,port)) 
        if result == 0: 
            print("Port {} is open".format(port)) 
        s.close() 
          
except KeyboardInterrupt: 
    print("\n Exitting Program !!!!") 
    sys.exit() 
except socket.gaierror: 
    print("\n Hostname Could Not Be Resolved !!!!") 
    sys.exit() 
except socket.error: 
    print("\n Server not responding !!!!") 
    sys.exit() 