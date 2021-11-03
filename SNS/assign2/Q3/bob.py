import socket

# public key
pk = {'v': 511594531302,
      'e': 5,
      'n': 6060711605323}


def authenticate_user_req(conn):
    status = True
    msg = "you need authentication ! "
    for i in range(2):
        msg += "send witness"
        conn.send(msg.encode())
        x = conn.recv(1024).decode()
        print("Input x : "+x)
        c = input("Enter challenge : ")
        conn.send(("c : "+c).encode())
        y = conn.recv(1024).decode()
        print("input y from alice  : "+y)

        c = int(c)
        x = int(x)
        y = int(y)
        if (pow(y, pk["e"])*pow(pk["v"], c)) % pk["n"] != x:
            conn.send("Sorry, ur authentication step failed!")
            status = False
            break
        else:
            msg = "last authentication  round is succesful"

    return status


# next create a socket object
s = socket.socket()

my_port_no = 12345

s.bind(('', my_port_no))

# put the socket into listening mode
s.listen(1)
print("online!")

# Establish connection with client.
conn, addr = s.accept()
print('Got connection from', addr)

status = authenticate_user_req(conn)
if status:
    conn.send(" Authentication succesful !".encode())
    print("bob : Authentication succesful !")
else:
    print("Authentication unsuccesful")
    conn.send(" Authentication unsuccesful !".encode())

# Close the connection with the client
conn.close()
s.close()
