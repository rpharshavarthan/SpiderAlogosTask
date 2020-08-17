#TASk-1(D)

n, r, x, y = map(int, input().split())
newr = r
c = list(map(int, input().split()))
s = list(map(int, input().split()))
for i in range(n):
    if c[i] == 1 and s[i] == 1:
        newr += x
    elif c[i] == 1 and s[i] == 0:
        newr -= y
if newr > r:
    print("promoted")
elif newr < r:
    print("demoted")
elif newr == r:
    print("no change")