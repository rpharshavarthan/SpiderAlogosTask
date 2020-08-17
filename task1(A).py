#TASK-1(A)
import math
n = int(input())
b = input()
if math.log2(int(b, 2)) - int(math.log2(int(b, 2))) == 0:
    print("-1")
elif math.log2(int(b, 2) + 1) - int(math.log2(int(b, 2) + 1)) == 0:
    print("-1")
else:
    s1 = bin(int(b, 2)-1)
    s2 = bin(int(b, 2)+1)
    print(s1[2:], s2[2:])