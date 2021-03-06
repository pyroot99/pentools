#!/usr/bin/env python3


def handler(socket):
    print("[i] Handling Connection")
    print("Enter bye to exit")
    while True:
        command = input("exec>> ")
        if command == "":
            continue
        if command != 'bye' and command != 'exit':
            socket.send_data(command)
            cmd_result = socket.receive_cmd_data()
            print(cmd_result.rstrip("\n"))
        else:
            socket.send_data(command)
            break
