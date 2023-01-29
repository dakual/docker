import socket
import json
import sys

HOST = 'localhost'
PORT = 5000

try:
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
  sys.stderr.write("[ERROR] %s\n" % msg[1])
  sys.exit(1)

try:
  sock.connect((HOST, PORT))
except socket.error as msg:
  sys.stderr.write("[ERROR] %s\n" % msg[1])
  sys.exit(2)

msg = {'@message': 'python test message 2', '@tags': ['python', 'test2']}

sock.send(str(json.dumps(msg) ).encode('utf-8') )

sock.close()
sys.exit(0)