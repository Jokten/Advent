import aoc, re
import time
data = aoc.get_data(2024,14).split("\n")
data = [re.findall(r"-?\d+",i) for i in data]
HEIGHT, WIDTH = 103, 101
safety = [0, 0, 0, 0]
t1 = time.time()
steps = 100
for i in data:
    px, py, vx, vy = int(i[0]), int(i[1]), int(i[2]), int(i[3])
    px = (px+vx*100)%WIDTH
    py = (py+vy*100)%HEIGHT
    quad = (px < WIDTH//2) + (py < HEIGHT//2)*2
    if px == WIDTH//2 or py == HEIGHT//2: continue
    safety[quad] += 1
s = 1
for i in safety:
    s*=i
print(s)
steps = 0
grid = 10
robs = [[int(i[0]), int(i[1]),int(i[2]), int(i[3])] for i in data]
nrobs = len(robs)
thres = (nrobs//grid)*2

t2 = time.time()
while True:
    safety2 = [0 for i in range(grid*grid)]
    steps += 1
    for i in robs:
        i[0] = (i[0]+i[2])%WIDTH
        i[1] = (i[1]+i[3])%HEIGHT
        qx = (i[0]*grid) // (WIDTH)
        qy = (i[1]*grid) // (HEIGHT)
        safety2[qy*grid+qx] += 1
    if any([1 if k>thres else 0 for k in safety2]):
        print(steps)
        break
print("Part 1 time: ",t2-t1)
print("Part 2 time: ",time.time()-t2)
