#!/usr/bin/env python3
import socket
DELIMITER = "<ENDING>"
CHUNK = 5*1024
class ClientHandler:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def Connect(self, server_ip, server_port):
        self.s.connect((server_ip, server_port))
        self.server_ip = server_ip
        self.server_port = server_port


    def send_data(self, data):
        self.data_bytes = data.encode('utf-8')
        self.s.send(self.data_bytes)

    def send_cmd_data(self, cmd_result):
        data = cmd_result + DELIMITER
        data_in_bytes = data.encode('utf-8')
        self.s.sendall(data_in_bytes)

    def receive_data(self):
        self.received_data_bytes = self.s.recv(CHUNK)
        self.received_data = self.received_data_bytes.decode('utf-8')
        return self.received_data


    def close(self):
        self.s.close()

