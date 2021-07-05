# If all ports are closed and 500 threads are used, it takes up to 5 minutes to scan all 65000 ports
import threading, socket, sys, time

hostname = "google.com"
arrPortsOpen = []
arrPortsClosed = []

startPort = 440
endPort = 450
# Use a max of 500 (my PC can do 916)
threads = 100

# Generate equal lists to scan (one list per thread)
seq = list(range(startPort, endPort))
avg = len(seq) / threads
arrPorts = []
last = 0.0

while last < len(seq):
    arrPorts.append(seq[int(last):int(last + avg)])
    last += avg


# DNS resolve hostname / ip address (ip stays the same)
try:
    target = socket.gethostbyname(hostname)
except:
    print("Host cannot be resolved")
    sys.exit(0)


class PortScan(threading.Thread):
    def __init__(self, portList):
        threading.Thread.__init__(self)
        self.portList = portList

    def run(self):
        try:
            # Scan every port in this thread
            for port in self.portList:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                # returns an error indicator
                result = s.connect_ex((target, port))
                if result == 0:
                    # Happens when the port is open
                    arrPortsOpen.append(port)
                else:
                    # Happens when the port is closed
                    arrPortsClosed.append(port)
                s.close()
        # Stop program when error
        except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
            sys.exit()
        except socket.error:
            print("\n Server not responding !!!!")
            sys.exit()


for i in arrPorts:
    # start the threads
    PortScan(i).start()


while True:
    # check if scan is finished
    # # if finished, print results sorted (threads can finish before each other when ports are open)
    time.sleep(1)
    if len(arrPortsClosed) + len(arrPortsOpen) == endPort - startPort:
        print("Open Ports: ", sorted(arrPortsOpen))
        print("Closed Ports: ", sorted(arrPortsClosed))
        break
