import aoc
def check(d):
    if d == sorted(d) or d == sorted(d, reverse=True):
        for i in range(len(d)-1): 
            if not (1 <= abs(d[i]-d[i+1]) <= 3): return 0
        else: return 1
    return 0
        
data = aoc.get_data(2024,2).split("\n")[:-1]
cnt, cnt2 = 0, 0
for i in data:
    d = list(map(int,i.split()))
    cnt += check(d)
    cnt2+= any(check(d[:j]+d[j+1:]) for j in range(len(d)))
    
print(cnt)
print(cnt2)