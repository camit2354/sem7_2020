p = 2267
q = 103
e1 = 354
e2 = 1206
d = 30

pk = {
    "e1": 354,
    "e2": 1206,
    "p": 2267,
    "q": 103

}

sk = {
    'd': d
}

f = open("BT18CSE063_AC_C_Kg_output.txt", "w")
f.write(str(pk))
f.write('\n')
f.write(str(sk))
f.close()

print("public key : "+str(pk))
print("secret key : "+str(sk))
