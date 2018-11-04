#!/usr/bin/env pyhton3

import socket

response = """HTTP/1.1 200 ok
Content-Type: text/html

<html>
<body>
<h1>Shit will break</h1>

<p>some more shit</p>
<p>So now to figure out how to change the font and font size, with maybe some other formatting.</p>
<p>Too much shit, not enough fan.</p>
</body>
</html>
"""
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("0.0.0.0", 8080))
serversocket.listen(6)

while True:
    # establih a connection
    conn,addr = serversocket.accept()

    print("Got a connection form %s" % str(addr))

    conn.recv(4096)
    conn.send(response.encode('utf-8'))
    conn.close()
