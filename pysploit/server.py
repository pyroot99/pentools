#!/usr/bin/env python3
from server.connections import ServerHandler






if __name__ == "__main__":
    server_socket = ServerHandler()
    server_socket.CreateSocket("", 4444)
    server_socket.Listen()
    client_conn, _ = server_socket.AcceptConn()
    server_socket.send_data("Hi this is server")
    print(server_socket.receive_data())
    client_conn.close()
