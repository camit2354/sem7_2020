

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


p1 = 79
p2 = 67

n = pow(p1, 10)
s = p2
e = 4
v = mul_inverse(pow(s, e), n)

pk = {
    "n": n,
    "v": v,
    "e": e
}

sk = {
    "s": s
}

r = input("Enter random no(r) for witness : ")
# witness
x = pow(r, e) % n
print("Witness :"+str(x))

# challenge
c = input("Enter challenge c :")

# y-generation
y = (r*pow(s, c)) % n

# check for correctness
y2 = pow(y, e)*pow(v, c) % n
print(y2)
