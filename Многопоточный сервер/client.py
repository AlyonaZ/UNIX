import socket
sock = socket.socket()
sock.setblocking(1)
sock.connect(('10.38.165.12', 9090))
msg = "Hello!"
sock.send(msg.encode())
data = sock.recv(1024)
sock.close()
print(data.decode())