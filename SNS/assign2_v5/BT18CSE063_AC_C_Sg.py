import sys
import random
import ast
import socket

hashSize = 64  # 64 bit output of hash function

# calculating xor of two strings of binary number a and b


def xor(a, b):
    result = ""
    for i in range(len(a)):
        result = result + str(int(a[i]) ^ int(b[i]))
    return result


def stringToBinary(input_str):
    return ''.join(format(ord(i), '08b') for i in input_str)


def binaryToString(b):
    s = ""
    for i in range(len(b)/8):
        n = int(b[8*i])
        for j in range(1, 8):
            n = n * 2 + int(b[8*i+j])
        s = s + chr(n)

    return s

# Binary to decimal conversion


# def bin2dec(binary):

#     binary1 = binary
#     decimal, i, n = 0, 0, 0
#     while(binary != 0):
#         dec = binary % 10
#         decimal = decimal + dec * pow(2, i)
#         binary = binary//10
#         i += 1
#     return decimal

def bin2dec(binary):
    ret = 0
    for i in range(len(binary)):
        ret = ret*2 + int(binary[i])
    return ret


# Decimal to binary conversion


def dec2bin(num):
    res = bin(num).replace("0b", "")
    if(len(res) % 4 != 0):
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res


def padding(x, sz):
    for i in range(len(x), sz):
        x += '1'
    return x

# input : any size output : 64 bit
# Hexadecimal to binary conversion


def hex2bin(s):
    mp = {'0': "0000",
          '1': "0001",
          '2': "0010",
          '3': "0011",
          '4': "0100",
          '5': "0101",
          '6': "0110",
          '7': "0111",
          '8': "1000",
          '9': "1001",
          'A': "1010",
          'B': "1011",
          'C': "1100",
          'D': "1101",
          'E': "1110",
          'F': "1111"}
    bin = ""
    for i in range(len(s)):
        bin = bin + mp[s[i]]
    return bin

# Binary to hexadecimal conversion


def bin2hex(s):
    mp = {"0000": '0',
          "0001": '1',
          "0010": '2',
          "0011": '3',
          "0100": '4',
          "0101": '5',
          "0110": '6',
          "0111": '7',
          "1000": '8',
          "1001": '9',
          "1010": 'A',
          "1011": 'B',
          "1100": 'C',
          "1101": 'D',
          "1110": 'E',
          "1111": 'F'}
    hex = ""
    for i in range(0, len(s), 4):
        ch = ""
        ch = ch + s[i]
        ch = ch + s[i + 1]
        ch = ch + s[i + 2]
        ch = ch + s[i + 3]
        hex = hex + mp[ch]

    return hex


def hash(x):
    # print("hash input : "+bin2hex(x))
    rollno = 63
    rollno = padding(dec2bin(rollno), hashSize)
    ret = rollno

    temp = int(len(x) / hashSize)+3
    x = padding(x, hashSize*temp)

    start = 0
    end = hashSize
    for i in range(int(len(x)/hashSize)):
        ret = xor(ret, x[start:end])

    return ret


def get_random_r():
    r = random.randint(1, 30)
    print("random r : "+str(r))
    return r


def sign(msg, sk):
    p = pk["p"]
    e1 = pk["e1"]
    q = pk['q']

    r = get_random_r()
    d = sk['d']
    s1 = bin2dec(hash(stringToBinary(str(msg) + str(pow(e1, r) % p))))
    s2 = r + (d*s1) % q
    return {"s1": int(s1), "s2": int(s2)}


f = open("BT18CSE063_AC_C_Kg_output.txt", "r")
pk = str(f.readline())
sk = str(f.readline())
pk = ast.literal_eval(pk)
sk = ast.literal_eval(sk)
f.close()

# Enter message
f = open("BT18CSE063_AC_C_input.txt", "r")
msg = str(f.readline())
msg_str = msg
f.close()

print("************   Signature !  ****************")
# next create a socket object
s = socket.socket()
print("#     alice, online!")

print("\nsecret key : "+str(sk))

bob_port_no = 12345
s.connect(('127.0.0.1', bob_port_no))

temp_msg = s.recv(2048).decode()
print("bob : "+temp_msg)


print("\nDoc for sign : \n"+msg)
msg = stringToBinary(msg)

msg = bin2dec(msg)

sign_ = sign(msg, sk)
print("\nsignature : \n"+str(sign_))

pkt = {
    'msg': msg_str,
    'sign_': sign_
}

s.send(str(pkt).encode())
print("\n msg , sign sent for verification !\n")
s.close()
