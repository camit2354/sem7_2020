import socket
import random
import ast
import sys


f = open("BT18CSE063_EA_C_Kg_output.txt", "r")
pk = str(f.readline())
sk = str(f.readline())
pk = ast.literal_eval(pk)
sk = ast.literal_eval(sk)
f.close()


# secret key
print("\n secret key : "+str(sk))

# public key


def select_random_r():
    r = random.randint(1, 77)
    print("randomly selected r : "+str(r))
    return r


def send_witness(skt, r):
    x = str(pow(r, pk["e"]) % pk["n"])
    skt.send(x.encode())
    print("witness sent : "+str(x))
    return r


def send_y(skt, r, c):
    y = str((r*pow(sk["s"], c)) % pk["n"])
    skt.send(y.encode())
    print("y sent : "+str(y))
    return


def get_c(skt):
    c = skt.recv(1024).decode()
    print("c got : "+c)
    c = int(c)
    return c


def is_round_succesful(skt):
    status = skt.recv(1024).decode()
    print("status got  : "+status)
    status = int(status)
    if status == 1:
        return True
    else:
        return False


def make_auth_request(skt):
    for i in range(pk['e']):
        print("**********  round "+str(i)+"  ************")
        r = select_random_r()
        send_witness(skt, r)
        c = get_c(skt)
        send_y(skt, r, c)
        status = is_round_succesful(skt)
        if status == False:
            return status

    return True


# next create a socket object
s = socket.socket()
print("#     Alice , online! ")

bob_port_no = 12345
s.connect(('127.0.0.1', bob_port_no))
msg = s.recv(1024).decode()
print(msg)

status = make_auth_request(s)
if status:
    print("******  Authentication succesful ! *************")
else:
    print("*****   Authentication unsuccesful! *************")

s.close()

# Breaking once connection closed
