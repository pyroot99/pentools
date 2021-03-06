#!/usr/bin/env python3
import socket
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

FAIL = f"{Fore.YELLOW}[{Style.BRIGHT}{Fore.RED}+{Style.NORMAL}{Fore.YELLOW}]{Style.RESET_ALL}"
SUCCESS = f"{Fore.YELLOW}[{Style.BRIGHT}{Fore.GREEN}+{Style.NORMAL}{Fore.YELLOW}]{Style.RESET_ALL}"
CHUNK = 5*1024
DELIMITER = "<ENDING>"

class ServerHandler:
    def __init__(self):
        """
        This class creates a TCP Socket
        """
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def CreateSocket(self, ip = "", port=4444):
        self.server_port = port
        self.server_ip = ip
        self.socket_address = (self.server_ip, self.server_port)
        self.s.bind(self.socket_address)


    def Listen(self, backlog = 5):
        self.s.listen(backlog)


    def AcceptConn(self):
        self.client_socket, self.client_address = self.s.accept()
        print(f"{SUCCESS} Connections Recieved from {self.client_address}")
        return (self.client_socket, self.client_address)


    def send_data(self, user_data):
        user_data_bytes = user_data.encode('utf-8')
        self.client_socket.send(user_data_bytes)


    def receive_data(self):
        received_data_bytes = self.client_socket.recv(CHUNK)
        self.data = received_data_bytes.decode('utf-8')
        return self.data


    def receive_cmd_data(self):
        result = b''
        while True:
            chunk = self.client_socket.recv(CHUNK)
            if chunk.endswith(DELIMITER.encode('utf-8')):
                chunk = chunk[:-len(DELIMITER)]
                result += chunk
                break
            result += chunk
        return result.decode('utf-8')



    def close(self):
        self.s.close()












