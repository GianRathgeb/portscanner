import socket
import sys

def fnScanPort(hostname, port):
    if not isinstance(port, int):
        port = int(port)
    target = socket.gethostbyname(hostname)

    try: 
        #! Code for multi port scan
        ''' code to check multiple ports
        # will scan ports between 1 to 65,535 
        for port in range(79, 81): 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            print(f'Checking port {port}')
            
            # returns an error indicator 
            result = s.connect_ex((target,port)) 
            if result == 0: 
                print("Port {} is open".format(port)) 
            s.close() 
        '''    


        #! Code for single port scan
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        print(f'Checking port {port}')
                
        # returns an error indicator 
        result = s.connect_ex((target,port)) 
        if result == 0: 
            print(f"Port {port} is open") 
        else:
            print(f"Port {port} is closed")
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