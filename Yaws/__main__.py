#!/usr/bin/env pyhton3
import Yaws.http as http
import socket

response_top = """HTTP/1.1 200 ok
Content-Type: text/html

<html>
<body>
<h1>Shit will break</h1>

<p>some more shit</p>
<p>So now to figure out how to change the font and font size, with maybe some other formatting.</p>
<p>Too much shit, not enough fan.</p>
"""

response_bottom = """</body>
</html>
"""
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("0.0.0.0", 8080))
serversocket.listen(6)

while True:
    # establih a connection
    conn,addr = serversocket.accept()

    print("Got a connection form %s" % str(addr))
    
    response = response_top

    request = http.Request(conn)

    # to do proccess request

    for key, value in request.headers.items():
        response+= "<li><b>" + key + "</b>:" + value + "</li>\n"

    response+= response_bottom
    conn.send(response.encode('utf-8'))
    conn.close()
