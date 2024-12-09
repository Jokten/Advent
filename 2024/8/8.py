mp = {}
bnds = set()
for e1,i in enumerate(open("./2024/8/input.txt", "r").readlines()):
    i = i.strip()
    for e2, j in enumerate(i):
        if j not in mp: mp[j] = [e1*1j+e2]
        else: mp[j].append(e1*1j+e2)
        bnds |= {e1*1j+e2}

anti = set()
anti2 = set()
for freq, cords in mp.items():
    if freq == ".": continue
    for i in range(len(cords)):
        for j in range(i+1,len(cords)):
            d = cords[i] - cords[j]
            a = cords[i]
            cnt = 0
            anti |= {a+d, a-2*d}&bnds
            while True:
                anti2 |= {a-cnt*d, a+cnt*d}&bnds
                cnt += 1
                if not {a-cnt*d, a+cnt*d}&bnds: break


print(len(anti), len(anti2))
