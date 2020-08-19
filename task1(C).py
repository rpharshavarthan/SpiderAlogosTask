#TASK1-(C)-INTERACTIVE PROBLEM

import random
a = [10, 8, 7, 16, 9, 43]
b = a[:]
random.shuffle(a)      #ADVAY'S SEQUENCE
d = {}
for i in range(6):
    for j in range(i + 1, 6):
        d[b[i] * b[j]] = [b[i], b[j]]

for i in range(4):
    x, y = map(int, input())
    ans = a[x] * a[y]
    print(ans)
    l = d[ans]
    i1 = b.index(l[0])
    f = b.pop(x)
    b.insert(x, l[0])
    b[i1] = f
    i2 = b.index(l[1])
    s = b.pop(y)
    b.insert(y, l[1])
    b[i2] = s

print("ADVAY'S ARRAY: ", a)
print("ADIT'S GUESS: ", b)