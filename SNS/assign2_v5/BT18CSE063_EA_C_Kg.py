import random


def isPrime(k):
    if k == 2 or k == 3:
        return True
    if k % 2 == 0 or k < 2:
        return False
    for i in range(3, int(k**0.5)+1, 2):
        if k % i == 0:
            return False

    return True


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


primes = []
for i in range(2, 100000):
    if isPrime(i):
        primes.append(i)

p1 = primes[random.randint(1, len(primes)-1)]
p2 = primes[random.randint(1, len(primes)-1)]

n = p1
s = p2
e = random.randint(5, 10)
v = mul_inverse(pow(s, e), n)

pk = {
    "n": int(n),
    "v": int(v),
    "e": int(e)
}

sk = {
    "s": int(s)
}


f = open("BT18CSE063_EA_C_Kg_output.txt", "w")
f.write(str(pk))
f.write('\n')
f.write(str(sk))
f.close()

print("public key : "+str(pk))
print("secret key : "+str(sk))
