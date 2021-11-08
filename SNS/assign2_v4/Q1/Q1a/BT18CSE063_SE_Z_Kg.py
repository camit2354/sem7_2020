import random
rollno = 63


def genrateRandomKey(rollno):
    n = random.randint(1, rollno*1000)
    return n


key1 = genrateRandomKey(rollno)
key2 = genrateRandomKey(rollno)

f = open("BT18CSE063_SE_Z_Kg_output.txt", "w")
print("\nfiestal cipher key1 :"+str(key1))
f.write(str(key1))
f.write('\n')
print("fiestal cipher key2 :"+str(key2))
f.write(str(key2))

f.close()
