#TASK-1(B)
n = int(input())
s = input()
dos = 0
for i in range(len(s)//2):
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:]
    if s1 == s2:
        dos += 1
        s = s1
    else:
        break
print(dos)