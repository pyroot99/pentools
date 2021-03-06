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


def start_server(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((socket.gethostname(), port))
        s.listen(1)
        conn, addr = s.accept()
        print(success + " Connection Recieved from " + f"{Fore.BLUE}" + addr[0] + f"{Fore.RESET}")
        conn.send(f"{Fore.GREEN}Hello from the server!!{Fore.RESET}".encode('utf-8'))
        while True:
            data = conn.recv(1024).decode('utf-8')
            conn.send(f"{Fore.GREEN}Data Recieved{Fore.RESET}".encode('utf-8'))
            if data != "bye":
                print(data)
            else:
                conn.close()
    except:
        conn.close()



if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)
    else:
        port = int(sys.argv[1])
        start_server(port)
