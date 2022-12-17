import numpy as np
import time
from functools import cache

@cache
def orientations(vect):
    x = vect[0]
    y = vect[1]
    z = vect[2]
    return (x, y, z), (-y, x, z), (-x, -y, z), (y, -x, z), (y, x, -z), (x, -y, -z), (-y, -x, -z), (-x, y, -z), (y, z, x), (
    z, -y, x), (-y, -z, x), (-z, y, x), (z, y, -x), (y, -z, -x), (-z, -y, -x), (-y, z, -x), (z, x, y), (x, -z, y), (
           -z, -x, y), (-x, z, y), (x, z, -y), (z, -x, -y), (-x, -z, -y), (-z, x, -y)


def main():
    with open(r'2021\19\input.txt', 'r') as file:
        data = file.read()
    worked_data = [i.splitlines() for i in data.split('\n\n')]
    scanners = []
    for scanner in worked_data:
        p = set()
        for i in scanner[1:]:
            p.add(eval(f'({i})'))
        scanners.append(p)
    print(len(scanners))
    full_map = scanners[0]
    scanner_left = scanners[1:].copy()
    scanner_left_new = []
    scanner_pos = set()
    while len(scanner_left) != 0:
        print(len(scanner_left))
        for scanner in scanner_left:
            print('nästa')
            matched = 0
            for scan_beacon in scanner:
                for beacon in sorted(list(full_map),key=lambda k: abs(k[0])+abs(k[1])+abs(k[2]))[-100:]:
                    for e, ori in enumerate(orientations(scan_beacon)):
                        diffx = ori[0] - beacon[0]
                        diffy = ori[1] - beacon[1]
                        diffz = ori[2] - beacon[2]
                        match = 0
                        new = set()
                        for i in scanner:
                            vect = orientations(i)[e]
                            mov_vect = (vect[0]-diffx, vect[1]-diffy, vect[2]-diffz)
                            new.add(mov_vect)
                            if mov_vect in full_map:
                                match += 1
                        if match >= 12:
                            full_map = full_map.union(new)
                            scanner_pos.add((diffx,diffy,diffz))
                            print('match!')
                            matched = 1
                            break
                    if matched:
                        break
                if matched:
                    break
            if not matched:
                scanner_left_new.append(scanner)
        scanner_left = scanner_left_new.copy()
        print(len(full_map))
        scanner_left_new = []
    print(len(full_map))
    ocean_size = 0
    for first in scanner_pos:
        for second in scanner_pos:
            size = abs(first[0]-second[0]) + abs(first[1]-second[1]) + abs(first[2]-second[2])
            if size > ocean_size:
                ocean_size = size
    print(ocean_size)
    print(scanners_tested)

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    print(f'Finished in {round(time.perf_counter()-start, 2)} second(s)')