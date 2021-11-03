import hashlib
import random

rollno = 63

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


def xor(a, b):
    result = ""
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result


def f(pt, key):
    temp = ""
    for i in range(int(len(pt)/8)):
        n = (key * rollno*i + rollno + key) % 128
        temp += chr(n)
    temp = stringToBinary(temp)
    result = xor(pt, temp)
    return result


def fiestal_round(l, r, key):
    l = xor(l, f(r, key))
    return l, r


def encode(l, r, key1, key2):
    r, l = fiestal_round(l, r, key1)
    l, r = fiestal_round(l, r, key2)
    return l, r


def decode(l, r, key1, key2):
    r, l = fiestal_round(l, r, key2)
    l, r = fiestal_round(l, r, key1)
    return l, r


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


def ptHalves(pt):
    pt_length = len(pt)
    l = pt[0:pt_length/2]
    r = pt[pt_length/2:pt_length]
    return l, r


def genrateRandomKey(rollno):
    n = random.randint(1, rollno*1000)
    return n


pt = input("Enter string : ")
pt = stringToBinary(pt)
print("Plain text in hex format : " + bin2hex(pt))

l, r = ptHalves(pt)

key1 = genrateRandomKey(rollno)
key2 = genrateRandomKey(rollno)

l, r = encode(l, r, key1, key2)
ct = l+r
print("* cipher test in hex format : " + bin2hex(ct))

l, r = decode(l, r, key1, key2)
pt = l+r
print("* plain test in hex format  : " + bin2hex(pt))
print("plain text in original char format : "+binaryToString(pt))
