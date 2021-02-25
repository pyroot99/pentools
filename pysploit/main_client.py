#!/usr/bin/env python3
from client.connections import ClientHandler
from client.handler import handler



if __name__ == "__main__":
    client_socket = ClientHandler()
    client_socket.Connect("127.0.0.1", 4444)
    handler(client_socket)
    client_socket.close()

