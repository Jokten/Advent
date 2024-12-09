def f(i,v,s,p): return s==v[0] if i==len(v) else any(f(i+1,v,j,p) for j in [s+v[i], s*v[i], int(f"{s}{v[i]}")][:2+p])
print(list(sum(i[0]for i in [tuple(map(int,l.replace(":","").split()))for l in open("./2024/7/input.txt")] if f(2,i,i[1],k))for k in [1,0]))

