#TASK1-(C)-INTERACTIVE PROBLEM

import random
a = [10, 8, 7, 16, 9, 43]
b = a[:]
random.shuffle(a)      # shuffles the list a. let us suppose this is ADVAY'S SEQUENCE
d = {}
for i in range(6):                      # it stores the product of all possible combinations of two numbers of the list
    for j in range(i + 1, 6):           # given in the question in dictionary d. key = product of two numbers, value = list of those two numbers
        d[b[i] * b[j]] = [b[i], b[j]]
for i in range(4):
    x, y = map(int, input())
    ans = a[x] * a[y]
    print(ans)         #from the answer we get from advay we can find those two numbers which gives this product.
    l = d[ans]         #those two numbers are stored in dictionary as the value of ans
    i1 = b.index(l[0])    #from here swapping happens in list b
    f = b.pop(x)          # those two numbers(for example 7 and 8) are stored at x and y and the numbers at x and y (for example 10 and 43)
    b.insert(x, l[0])     # are stored at b.index(7) and b.index(8)
    b[i1] = f
    i2 = b.index(l[1])
    s = b.pop(y)
    b.insert(y, l[1])
    b[i2] = s

print("ADVAY'S ARRAY: ", a)
print("ADIT'S GUESS: ", b)
