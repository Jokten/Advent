import time

def main():
    with open(r".\2023\5\input.txt") as f:
        lines = f.read()
    data = lines.split("\n\n")
    data = [i.splitlines() for i in data]
    seeds = data[0]
    maps = [i[1:] for i in data[1:]]

    for i in range(len(maps)):
        maps[i] = [j.split(" ") for j in maps[i]]
        for j in range(len(maps[i])):
            maps[i][j] = [int(k) for k in maps[i][j]]

    # Makes into ranges
    temp = []
    for i in range(len(maps)):
        temp.append([])
        for j in range(len(maps[i])):
            temp[i].append((maps[i][j][1],maps[i][j][1]+maps[i][j][2]-1,maps[i][j][0],maps[i][j][0]+maps[i][j][2]-1))
    maps = temp


    seeds = [i.split(' ') for i in seeds]
    seeds = [int(i) for i in seeds[0][1:]]
    dests = []
    # P1
    for i in range(len(seeds)):
        curr = seeds[i]
        for j in range(len(maps)):
            for curr_map in maps[j]:
                if curr_map[0] <= curr <= curr_map[1]:
                    curr = curr_map[2] + curr - curr_map[0]
                    break
        dests.append(curr)
    print(min(dests))

    # P2
    seeds = [(i[0],i[0]+i[1]-1) for i in zip(*(iter(seeds),) * 2)] # Turns into tuples with (min,max)
    lowest = 1000000   # Arbitrary large number
    lows = []
    start_time = time.time()
    for i in range(len(seeds)):
        drange = [seeds[i]]
        for j in range(len(maps)):
            mapped_range = []
            rest_range = []
            for curr_map in maps[j]:
                for curr_seed in drange:
                    min_diff, max_diff = curr_seed[0] - curr_map[0], curr_map[1] - curr_seed[1]
                    min_src, max_src = curr_map[0], curr_map[1]
                    min_dest, max_dest = curr_map[2], curr_map[3]

                    if (curr_seed[0] < min_src and curr_seed[1] < min_src) or (curr_seed[0] > max_src and curr_seed[1] > max_src):
                        rest_range.append(curr_seed)

                    elif min_diff >= 0:
                        if max_diff >= 0:
                            mapped_range.append((min_dest+min_diff,max_dest-max_diff))
                        else:
                            mapped_range.append((min_dest+min_diff,max_dest))
                            rest_range.append((max_src+1,max_src-max_diff))
                    else:
                        if max_diff >= 0:
                            mapped_range.append((min_dest,max_dest-max_diff))
                            rest_range.append((min_src+min_diff,min_src-1))
                        else:
                            mapped_range.append((min_dest,max_dest))
                            rest_range.append((min_src+min_diff,min_src-1))
                            rest_range.append((max_src+1,max_src-max_diff))

                drange = rest_range
                rest_range = []
            drange += mapped_range
        lowest = min([i[0] for i in drange])
        lows.append(lowest)
    print(min(lows))
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
