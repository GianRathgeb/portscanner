import socket
import sys


def fnScanPort(hostname, lowestPort, highestPort):
    if not isinstance(lowestPort, int):
        lowestPort = int(lowestPort)
    if not isinstance(highestPort, int):
        highestPort = int(highestPort)
    target = socket.gethostbyname(hostname)
    try:
        for port in range(lowestPort, highestPort + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(f'Checking port {port}')

            # returns an error indicator
            result = s.connect_ex((target, port))
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
