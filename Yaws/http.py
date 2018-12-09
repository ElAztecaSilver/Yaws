class Request:
    def __init__ (self, sock):
        request_text = sock.recv(4096).decode("utf-8")
        request_lines = request_text.splitlines()
        first_line = request_lines[0].split()
        self.method = first_line[0]
        self.path = first_line[1] 

        self.headers = {}
        for line in request_lines[1:-1]:
            key, value = line.split(": ", maxsplit=1)
            self.headers[key] = value