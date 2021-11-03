# Binary to decimal conversion
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


def bin2dec(binary):

    ret = 0
    for i in range(len(binary)):
        ret = ret*2 + int(binary[i])
    return ret


def dec2bin(decimal):
    ret = ""
    i = 0
    done = False
    while not done:
        if decimal != 0 or (i % 8 != 0):
            ret += decimal % 2
            decimal /= 2
            i += 1
        else:
            done = True
    return ret


def hash(x):
    ret = ""
    start = 0
    end = 8
    sz = 10
    if len(x)/8 > sz:
        for i in range(sz):
            n = bin2dec(x[start:end])
            start += 8
            end += 8
            ret += str(n % 2)
    else:
        for i in range(len(x)/8):
            n = bin2dec(x[start:end])
            start += 8
            end += 8
            ret += str(n % 2)
        for i in range(len(x)/8, sz):
            ret += '0'
    return ret


def verify(pk, msg, sign):
    e1 = pk["e1"]
    e2 = pk["e2"]
    p = pk["p"]
    q = pk["q"]

    s1 = sign["s1"]
    s2 = sign["s2"]

    temp = pow(e1, s2) * pow(e2, -1*s2) % p
    v = bin2dec(hash(stringToBinary(str(msg) + str(temp))))
    print("v :"+str(v)+" s1 : " + str(s1))
    return v == s1


def sign(msg, d, r, pk):
    p = pk["p"]
    e1 = pk["e1"]
    s1 = bin2dec(hash(stringToBinary(str(msg) + str(pow(e1, r) % p))))
    s2 = r + (d*s1) % q
    return {"s1": s1, "s2": s2}


p = 2267
q = 103
e1 = 354
d = 30
e2 = 1206
r = 11

pk = {
    "e1": e1,
    "e2": e2,
    "p": p,
    "q": q


}

msg = 99887766554433
sign_ = sign(msg, d, r, pk)
print(sign_)

result = verify(pk, msg, sign_)
print(result)
