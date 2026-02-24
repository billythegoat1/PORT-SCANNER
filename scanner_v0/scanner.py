import socket

from colorama import init, Fore


init()
GREEN=Fore.GREEN
RESET=Fore.RESET
GRAY=Fore.LIGHTBLACK_EX


def check_port(target, port):

    try:
        #Create a socket object

        #AF_INET Specifies IPv4
        # SOCK_STREAM specifies that it is a TCP connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #close the connection if the 
        s.settimeout(1)

        #connect_ex returns 0 if the connection was successfully created and 9 if there is an error
        connect_result = s.connect_ex((target, port))

        #After confirming the port is open, close the connection
        s.close()

        return connect_result == 0

    except:
        return False


#Enter your target hostname or IP address
target='scanme.nmap.org'
port=80


if check_port(target, port):
    print(f'{GREEN}[+] {target}:{port} is OPEN!    {RESET}')
else:
    print(f'{GRAY}[+] {target}:{port} is CLOSED!    {RESET}', end="\r")
