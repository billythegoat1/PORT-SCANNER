#! /usr/bin/env python3

import socket
import sys
import os

sys.path.append(os.path.abspath('..'))

from ports import COMMON_PORTS
from colorama import init, Fore
import pyfiglet
from datetime import datetime

init()
GREEN = Fore.GREEN
GRAY = Fore.RESET

banner = pyfiglet.figlet_format('Port Scanner V 1.0')
print(banner)



if len(sys.argv) == 2:
    
    target = socket.gethostbyname(sys.argv[1])

else:
    print("Enter a valid hostname !!")
    sys.exit()

print('#' * 50)
print("Scanning Target: " + target)
print("Scanning started at: ", datetime.now())
print('#' * 50)

try:

    for port in COMMON_PORTS:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        try:
            result = s.connect_ex((target, port))

            if result == 0:
                service = socket.getservbyport(port,'tcp')
                print(f"Port {GREEN}[+]{port}/{service}{GRAY} is open.")           

            else:
                print(f'Port {port} is closed.')
        
        except OSError:
            print(f"OSError: {OSError} on port {port}.")
        finally:
            s.close()


except KeyboardInterrupt:
    print("\n Exiting Program !!")
    sys.exit()

except socket.gaierror:
    print('\n Hostname could not be resolved.')
    sys.exit()

except socket.error:
    print('Server not responding !!')
    sys.exit()