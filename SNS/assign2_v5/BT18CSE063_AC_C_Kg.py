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


def getFactors(n):
    facts = []
    for i in range(2, n):
        if isPrime(i) and n % i == 0:
            facts.append(i)
    return facts


def get_e0(p):
    facts_phi = getFactors(p-1)

    for i in range(2, p-1):
        status = True
        for j in range(len(facts_phi)):
            if pow(i, facts_phi[j]) % p == 1:
                status = False
                break
        if status:
            return i

    return -1


def get_e1(e0, p, q):
    return int(pow(e0, p-1/q) % p)


primes = []
for i in range(2, 5000):
    if isPrime(i):
        primes.append(i)


p = primes[random.randint(1, len(primes)-1)]

primeFactors = getFactors(p-1)
q = primeFactors[random.randint(1, len(primeFactors)-1)]


e0 = get_e0(p)

e1 = get_e1(e0, p, q)

d = random.randint(2, p-1)
e2 = pow(e1, d) % p


pk = {
    "e1": int(e1),
    "e2": int(e2),
    "p": int(p),
    "q": int(q)

}

sk = {
    'd': int(d)
}

f = open("BT18CSE063_AC_C_Kg_output.txt", "w")
f.write(str(pk))
f.write('\n')
f.write(str(sk))
f.close()

print("public key : "+str(pk))
print("secret key : "+str(sk))
