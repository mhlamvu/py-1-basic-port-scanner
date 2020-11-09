#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# AF_INET - ipv4 address
# SOCK_STREAM - refers to using TCP packets so perform the connection

host = "<target host here>"
port = "<port you want to scan here>"


def basic_port_scanner(port):
    if s.connect_ex((host, port)):
        print("Port %d closed" % (port))
    else:
        print("Port %d open" % (port))


basic_port_scanner(port)
