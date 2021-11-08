import random


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


def gen_random_key_64():
    key = ""
    for i in range(64):
        n = random.randint(0, 1)
        key += str(n)
    return key


key = gen_random_key_64()
key = bin2hex(key)
print("\n key generated : "+key)
f = open("BT18CSE063_SE_C_Kg_output.txt", "w")
f.write(key)
f.close()
