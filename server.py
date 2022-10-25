import socket

s = socket.socket()
print("Socket created")

s.bind(("localhost",9999))

s.listen(3)
print("waiting for connections")

while True:
    c, addr = s.accept()
    name = ""
    name = c.recv(1024).decode()
    print("connected with ", addr, name)
    c.send(bytes("Wellcome " + name,"utf-8"))
    c.close()
