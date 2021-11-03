import hashlib


def xor(a, b):
    result = ""
    for i in range(len(a)):
        result = result + str(int(a[i]) ^ int(b[i]))
    return result


def f(pt, key):
    result = ""
    for i in range(len(pt)):
        if pt[i] == '0':
            x = 0
        else:
            x = (int(key) + int("63") + i) % 2
        result = result + str(x)
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


str1 = input("Enter string : ")
str1 = stringToBinary(str1)
print("Plain text :" + str1)

l, r = ptHalves(str1)

key1 = input("Enter key1 for fiestal cipher :")
key2 = input("Enter key2 for fiestal cipher :")

l, r = encode(l, r, key1, key2)
ct = l+r
print("cipher test :" + binaryToString(ct))

l, r = decode(l, r, key1, key2)
pt = l+r
print("plain test :" + binaryToString(pt))
