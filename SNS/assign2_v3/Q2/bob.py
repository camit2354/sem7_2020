import sys
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
        x += '0'
    return x

# input : any size output : 64 bit


def hash(x):
    rollno = 63
    rollno = padding(dec2bin(rollno), hashSize)
    ret = rollno

    temp = int(len(x) / hashSize)+1
    x = padding(x, hashSize*temp)

    start = 0
    end = hashSize
    for i in range(int(len(x)/hashSize)):
        ret = xor(ret, x[start:end])

    return ret


def ext_eucledian(a, b):
    if a == 0:
        return [0, 1]
    else:
        x1, y1 = ext_eucledian(b % a, a)
        x = y1 - int(b/a)*x1
        y = x1

        return [x, y]


def mul_inverse(a, m):
    x, y = ext_eucledian(a, m)
    if x < 0:
        x = m + x
    return x


def verify(pk, msg, sign):
    e1 = pk["e1"]
    e2 = pk["e2"]
    p = pk["p"]
    q = pk["q"]
    s1 = sign["s1"]
    s2 = sign["s2"]

    temp = pow(e1, s2) * pow(mul_inverse(e2, p), s2) % p
    v = bin2dec(hash(stringToBinary(str(msg) + str(temp))))
    print("v :"+str(v)+" s1 : " + str(s1))
    return v == s1


pk = {
    "e1": 354,
    "e2": 1206,
    "p": 2267,
    "q": 103

}

msg = sys.argv[1]
s1 = int(sys.argv[2])
s2 = int(sys.argv[3])

print("doc for verify : "+msg)

sign_ = {
    "s1": s1,
    "s2": s2
}

print("signature on given doc  : "+str(sign_))

msg = stringToBinary(msg)
msg = bin2dec(msg)
print("msg : "+str(msg))
result = verify(pk, msg, sign_)
print("verification result : "+str(result))
