import socket
import sys


def fnScanPort(hostname, port):
    # check if port is integer
    if not isinstance(port, int):
        port = int(port)
    # DNS resolve hostname / ip address (ip stays the same)
    target = socket.gethostbyname(hostname)

    try:
        # make tcp connection to port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f'Checking port {port}')

        # returns an error indicator
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
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
