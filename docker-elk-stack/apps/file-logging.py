import socket

host = "localhost"
port = 5000


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))

    with open("file.log", mode="rb") as f:
        for line in f.readlines():
            sock.send(line)
    print("all data sent to Logstash")