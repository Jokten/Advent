import re
import functools
with open("./2024/5/input.txt", "r") as f:
    rules, update = f.read().split("\n\n")
rules = [list(map(int, re.findall(r"\d+", i))) for i in rules.split("\n")]
update = [list(map(int, re.findall(r"\d+", i))) for i in update.split("\n")]

def comp(b,a):
    if [a,b] in rules: return 1
    elif [b,a] in rules: return -1
    
update = update[:-1]
cnt = 0
cnt2 = 0
d = [i.copy() for i in update]

keyf = functools.cmp_to_key(comp)
for i in update:
    ss = sorted(i, key=keyf)
    if ss in d:
        cnt += ss[len(ss)//2]
    else:  cnt2 += ss[len(ss)//2]
print(cnt)
print(cnt2)