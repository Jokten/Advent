import re
with open("./2024/1/input.txt", "r") as f:
    l = list(map(int,re.findall(r"\d+",f.read())))
    l1, l2 = sorted(l[0::2]), sorted(l[1::2])
    p1 = sum([abs(l1[i]-l2[i]) for i in range(len(l1))])
    p2 = sum([i*l2.count(i) for i in l1])
    print(p1, p2)
