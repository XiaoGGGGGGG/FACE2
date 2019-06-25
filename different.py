import sys

f1, f2 = None, None
try:
    f1 = open("pro1.txt", "r")
    m = f1.readlines()
except IOError:
    print
    "pro.txt does not exist!"
    sys.exit(2)
finally:
    if f1:
        f1.close()
# reead lines from mids2.txt
try:
    f2 = open("pro.txt", "r")
    n = f2.readlines()
except IOError:
    print
    "pro1.txt does not exist!"
    sys.exit(2)
finally:
    if f2:
        f2.close()
# filter
for a in m:
    for b in n:
        if a == b:
            n.remove(b)

for i in range(len(n)):
    n[i] = n[i].strip()
# print n
# print " ".join(n)
for aar in n:
    with open("baidu.txt", "a") as fe:
        fe.write(aar + "\n")
