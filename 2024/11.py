import aoc, collections

dic = collections.defaultdict(int)
for i in aoc.get_data(2024,11).split(): dic[int(i)] += 1

for i in range(75):
    for stone, c in tuple(dic.items()):
        if stone == 0:
            dic[1] += c
        elif len(str(stone))%2 == 0:
            mid = 10**(len(str(stone))//2)
            dic[stone//mid] += c
            dic[stone%mid] += c
        else:
            dic[stone*2024] += c
        dic[stone] -= c
print(sum(dic.values()))

