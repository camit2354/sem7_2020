import socket

# secret key
sk = {'s': 79}

# public key
pk = {'v': 511594531302, 'e': 5, 'n': 6060711605323}


def send_witness(skt):
    r = int(input("Enter random no(r) for witness : "))
    x = str(pow(r, pk["e"]) % pk["n"])
    skt.send(x.encode())
    return r


def send_y(skt, r):
    c = int(input("Enter c got from alice : "))
    y = str((r*pow(sk["s"], c)) % pk["n"])
    skt.send(y.encode())
    return


def make_auth_request(s):
    r = 2
    while True:
        msg = s.recv(1024).decode()
        print(msg)
        ch = int(input("1.send witness 2.send y  3. exit  ->  "))
        if ch == 1:
            r = send_witness(s)
        elif ch == 2:
            send_y(s, r)
        else:
            break
    return


# next create a socket object
s = socket.socket()
print("online!")

bob_port_no = 12345
s.connect(('127.0.0.1', bob_port_no))

make_auth_request(s)

s.close()

# Breaking once connection closed
