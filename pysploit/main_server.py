#!/usr/bin/env python3
from server.connections import ServerHandler
from server.handler import handler




if __name__ == "__main__":
    server_socket = ServerHandler()
    server_socket.CreateSocket("", 4444)
    server_socket.Listen()
    print("[+] Waiting for connections")
    client_conn, _ = server_socket.AcceptConn()
    handler(server_socket)
    server_socket.close()
