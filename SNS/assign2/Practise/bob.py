import socket

# next create a socket object
s = socket.socket()

my_port_no = 12345

s.bind(('', my_port_no))

# put the socket into listening mode
s.listen(1)
print("online!")

# Establish connection with client.
c, addr = s.accept()
print('Got connection from', addr)

msg = input("bob : ")
c.send(msg.encode())

while True:
    msg = c.recv(1024).decode()
    if not msg:
        break
    print(msg)
    msg = input("bob : ")
    c.send(msg.encode())


# Close the connection with the client
c.close()
s.close()
