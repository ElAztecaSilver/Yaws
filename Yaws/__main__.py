#!/usr/bin/env pyhton3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("0.0.0.0", 8080))
serversocket.listen(6)

while True:
    # establih a connection
    conn,addr = serversocket.accept()

    print("Got a connection form %s" % str(addr))

    conn.send("Welcome to my server.".encode('utf-8'))
    conn.close()
