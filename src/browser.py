import socket
import sys
import ssl

# get url from arguments
def init():
    if __name__ == "__main__":
        load(sys.argv[1])

def load(url):
    headers, body = request(url)
    assert "transfer-encoding" not in headers
    assert "content-encoding" not in headers
    show(body)

def show(body):
    in_angle = False
    for char in body:
        if char == "<":
            in_angle = True
        elif char == ">":
            in_angle = False
        elif not in_angle:
            print(char, end="")

def request(url):
    scheme, url = url.split("://", 1)
    assert scheme in ["http", "https"], "Unknown scheme {}".format(scheme)
   

    host, path = url.split("/", 1)
    path = "/" + path
    
    port = 80 if scheme == "http" else 443
    if ":" in host:
        host, port = host.split(":", 1)
        port = int(port)

    s = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_STREAM,
        proto=socket.IPPROTO_TCP,
    )

    s.connect((host, port))
    if scheme == "https":
        ctx = ssl.create_default_context()
        s = ctx.wrap_socket(s, server_hostname=host)

    s.send("GET {} HTTP/1.0\r\n".format(path).encode("utf8") + 
       "Host: {}\r\n\r\n".format(host).encode("utf8"))
    
    response = s.makefile("r", encoding="utf8", newline="\r\n")
    statusline = response.readline()
    version, status, explanation = statusline.split(" ", 2)
    assert status == "200", "{}: {}".format(status, explanation)
    
    headers = {}
    for line in response:
        # skip newlines
        if line == "\r\n": break
        header, value = line.split(":", 1)
        headers[header.lower()] = value.strip()

    body = response.read()
 
    s.close()

    return headers, body
    # return {}, ''

init()