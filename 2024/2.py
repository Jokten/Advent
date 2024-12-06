
def check(d):
    if d == sorted(d) or d == sorted(d, reverse=True):
        for i in range(len(d)-1): 
            if not (1 <= abs(d[i]-d[i+1]) <= 3): return 0
        else:
            return 1
    return 0
        
with open("input.txt", "r") as f:
    data = f.readlines()
    cnt = 0
    cnt2 = 0
    for i in data:
        d = list(map(int,i.split()))
        cnt += check(d)
        for j in range(len(d)):
            if check(d[:j]+d[j+1:]):
                cnt2 += 1
                break

    print(cnt)
    print(cnt2)