import socket
import random
import ast
import sys


# public key
f = open("BT18CSE063_EA_C_Kg_output.txt", "r")
pk = str(f.readline())
pk = ast.literal_eval(pk)
f.close()


def select_random_c(e):
    c = random.randint(1, e)
    print("randomly selected c : "+str(c))
    return c


def get_witness(conn):
    x = conn.recv(1024).decode()
    print("Witness got : "+x)
    x = int(x)
    return x


def get_y(conn):
    y = conn.recv(1024).decode()
    print("y got : "+y)
    y = int(y)
    return y


def is_valid_y(y, x, c):
    e = pk['e']
    v = pk['v']
    n = pk['n']
    y2 = (pow(y, e)*pow(v, c)) % n
    print("y2 : "+str(y2)+" x : "+str(x))
    if y2 == x:
        print("valid y !")
        return True
    else:
        print("Invalid y !")
        return False


def send_c(conn, c):
    conn.send(str(c).encode())
    return


def send_round_status(conn, status):
    if status:
        conn.send('1'.encode())
    else:
        conn.send('0'.encode())


def authenticate_user_req(conn):
    e = pk['e']
    for i in range(e):
        print("**********  round "+str(i)+"  ************")
        x = get_witness(conn)
        c = select_random_c(e)
        send_c(conn, c)
        y = get_y(conn)
        status = is_valid_y(y, x, c)
        send_round_status(conn, status)
        if status == False:
            return status

    return True


# next create a socket object
s = socket.socket()

my_port_no = 12345

s.bind(('', my_port_no))

# put the socket into listening mode
s.listen(1)
print("#     bob, online!")

# Establish connection with client.
conn, addr = s.accept()
print('Got connection from', addr)
conn.send("Auth required !".encode())

status = authenticate_user_req(conn)
if status:
    print("***********    Auth success !      ****************")
else:
    print("***********    Auth failed         ****************")

# Close the connection with the client
conn.close()
s.close()
