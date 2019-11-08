#!/usr/bin/env python3.8

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65433        # Port to listen on (non-privileged ports are > 1023)

with socket.create_server(addr) as s:
    conn, addr = s.accept()
    with conn:
        print('Connected by', (HOST, PORT))
        while True:
            data = conn.recv(1024)
            print("Yasuko's server got this message: {}".format(data))
            if not data:
                break
            conn.sendall(data)
