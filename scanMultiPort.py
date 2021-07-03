import socket
import sys
import time

# TODO: use threads to perform multiple portscanns at the same time, use array to store and sort results

def fnScanPort(hostname, lowestPort, highestPort, speed):
    # Check if ports are integers
    if not isinstance(lowestPort, int):
        lowestPort = int(lowestPort)
    if not isinstance(highestPort, int):
        highestPort = int(highestPort)
    # DNS resolve hostname / ip address (ip stays the same)
    target = socket.gethostbyname(hostname)
    # make tcp connection to every port in range
    try:
        for port in range(lowestPort, highestPort + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(f'Checking port {port}')

            # returns an error indicator
            result = s.connect_ex((target, port))
            if result == 0:
                # Happens when the port is open
                print("Port {} is open".format(port))
            else:
                # Happens when the port is closed
                print("Port {} is closed".format(port))
            s.close()
            time.sleep(speed)
    # Stop program when user interrupt or when error
    except KeyboardInterrupt:
        print("\n Exitting Program !!!!")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
    except socket.error:
        print("\n Server not responding !!!!")
        sys.exit()
