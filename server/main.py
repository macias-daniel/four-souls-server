from classes.Card import Card
from classes.Player import Player
import socket
from _thread import *
import sys

server = ""
# safe port to connect to
port = 5555
# Types of connection. Connection to an IPV4 address.
# Stream represents how server string comes in.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server and port to the socket. If the port is being used, it fails.
# Setting up a port to look for certain connections.
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# If left blank, it allows for unlimited connections to happen.
# The param indicates how many people can listen.
s.listen(2)
print("Waiting for a connection, Server Started")


# When connecting to a client, we want this to continually run.
def threaded_client(conn):
    reply = ""
    while True:
        try:
            data = conn.recv(2048 * 4)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))
        except:
            break


# Continually listen for connections.
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))
