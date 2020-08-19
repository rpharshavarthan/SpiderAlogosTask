#TASK-1(A)
#if we look at the binary numbers, length of a binary string increases by 1 at 2, 4, 8 and so on ie. at powers of 2
#so binary value of (2^n) and ((2^n) - 1) cannot be decomposed as the avg of two others
import math
n = int(input())
b = input()
if b == "0" or math.log2(int(b, 2)) - int(math.log2(int(b, 2))) == 0:       #checks if decimal value of bimary string is 2^n
    print("-1")
elif math.log2(int(b, 2) + 1) - int(math.log2(int(b, 2) + 1)) == 0: #checks if decimal value of binary string is ((2^n)-1)
    print("-1")
else:
    s1 = bin(int(b, 2)-1)
    s2 = bin(int(b, 2)+1)
    print(s1[2:], s2[2:])


