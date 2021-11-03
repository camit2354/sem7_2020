

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


p1 = 67
p2 = 79

n = pow(p1, 7)
s = p2
e = 5
v = mul_inverse(pow(s, e), n)

pk = {
    "n": n,
    "v": v,
    "e": e
}

sk = {
    "s": s
}

print("public key :"+str(pk))

print("secret key :"+str(sk))
