import socket
import sys

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
    assert url.startswith("http://")
    url = url[len("http://"):]
    host, path = url.split("/", 1)
    path = "/" + path

    s = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_STREAM,
        proto=socket.IPPROTO_TCP,
    )

    s.connect((host, 80))
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

init()