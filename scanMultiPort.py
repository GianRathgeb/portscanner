import socket
import sys


def fnScanPort(hostname, lowestPort, highestPort):
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
                print("Port {} is open".format(port))
            s.close()
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
