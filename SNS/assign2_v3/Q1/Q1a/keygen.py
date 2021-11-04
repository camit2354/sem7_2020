import random
rollno = 63


def genrateRandomKey(rollno):
    n = random.randint(1, rollno*1000)
    return n


key1 = genrateRandomKey(rollno)
key2 = genrateRandomKey(rollno)

print("key1 : "+str(key1))
print("key2 : "+str(key2))
