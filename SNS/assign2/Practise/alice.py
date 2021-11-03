import socket

# next create a socket object
s = socket.socket()
print("online!")


bob_port_no = 12345
s.connect(('127.0.0.1', bob_port_no))

while True:
    msg = s.recv(1024).decode()
    if not msg:
        break
    print(msg)
    msg = input("alice : ")
    s.send(msg.encode())


s.close()

# Breaking once connection closed
