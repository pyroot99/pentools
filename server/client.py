#!/usr/bin/env python3
import socket
import colorama
import sys
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
success = f"{Fore.YELLOW}[{Style.BRIGHT}{Fore.GREEN}+{Style.NORMAL}{Fore.YELLOW}]{Style.RESET_ALL}"
fail = f"{Fore.YELLOW}[{Style.BRIGHT}{Fore.RED}+{Style.NORMAL}{Fore.YELLOW}]{Style.RESET_ALL}"

def usage():
    print(fail + " Usage: python3 " + sys.argv[0] + " <port>")
    print(fail + " Example: python3 " + sys.argv[0] + " 1234")


def start_conn(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), port))
    print(success + "Connected")
    header = s.recv(1024)
    print(header.decode('utf-8'))
    while True:
        data = input()
        if data != "bye":
            s.send(data.encode('utf-8'))
            print(s.recv(1024).decode('utf-8'))
        else:
            s.send(data.encode('utf-8'))
            s.close()
            break



if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)
    else:
        port = int(sys.argv[1])
        start_conn(port)
