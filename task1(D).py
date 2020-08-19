#TASk-1(D)
#adit can perform well if contest happens(1) and he eats SCN(1) on the day of contest
#he cannot perform well if contest happens(1) and he doesn't eats SCN(0) on the day of contest

n, r, x, y = map(int, input().split())
newr = r
c = list(map(int, input().split()))
s = list(map(int, input().split()))
for i in range(n):
    if c[i] == 1 and s[i] == 1:   #performs Well
        newr += x
    elif c[i] == 1 and s[i] == 0:   #doesn't performs well
        newr -= y
if newr > r:
    print("promoted")
elif newr < r:
    print("demoted")
elif newr == r:
    print("no change")