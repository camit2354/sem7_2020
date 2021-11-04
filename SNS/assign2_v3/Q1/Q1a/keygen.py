import random
rollno = 63


def genrateRandomKey(rollno):
    n = random.randint(1, rollno*1000)
    return n


key1 = genrateRandomKey(rollno)
key2 = genrateRandomKey(rollno)

f = open("keygen_output.txt", "w")
f.write(str(key1))
f.write('\n')
f.write(str(key2))

f.close()
