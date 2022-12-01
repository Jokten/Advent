import heapq
import copy
import numpy as np
cost = {1: 1, 2: 10, 3: 100, 4: 1000}


def flatten(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])

def possible_moves(cs, corr, nests):
    moves = []
    for e, i in enumerate(nests):

        if i[0] != 0 and (i[0] != e+1 or i[1] != e+1):
            possible = check_corr(corr, e)

            for j in possible:
                new_nest = copy.deepcopy(nests)

                new_nest[e][0] = 0

                new_corr = copy.deepcopy(corr)

                new_corr[j] = i[0]

                cos = cost[i[0]]
                s = cos*2*(int(abs(e+1.5-j))+1)
                if j in [0, 7]:
                    s -= cos
                moves.append((cs+s, new_corr, new_nest))
        elif (i[1] != 0) and i[1] != e+1 and i[0] == 0:
            possible = check_corr(corr, e)
            for j in possible:
                new_nest = copy.deepcopy(nests)
                new_nest[e][1] = 0
                new_corr = copy.deepcopy(corr)
                new_corr[j] = i[1]
                cos = cost[i[1]]
                s = cos + cos*2*(int(abs(e+1.5-j))+1)
                if j in [0, 7]:
                    s -= cos
                moves.append((cs+s, new_corr, new_nest))
    for e, i in enumerate(corr):
        pos2 = check_corr2(corr, e)

        if i and nests[i-1][1] == 0 and i in pos2:
            new_corr = copy.deepcopy(corr)
            new_corr[e] = 0
            new_nest = copy.deepcopy(nests)
            new_nest[i-1][1] = i
            cos = cost[i]
            s = cos + cos*2*(int(abs(e-0.5-i))+1)
            if e in [0, 7]:
                s -= cos
            moves.append((cs+s, new_corr, new_nest))
        elif i and nests[i-1][1] == i and nests[i-1][0] == 0 and i in pos2:
            new_corr = copy.deepcopy(corr)
            new_corr[e] = 0
            new_nest = copy.deepcopy(nests)
            new_nest[i-1][0] = i
            cos = cost[i]
            s = cos*2*(int(abs(e-0.5-i))+1)
            if e in [0, 7]:
                s -= cos
            moves.append((cs+s, new_corr, new_nest))
    return moves

def check_corr(corr, index):
    indl = index+1
    indr = index+2
    possible = []
    while True:
        if corr[indl] == 0 and indl != -1:
            possible.append(indl)
            indl -= 1
        else:
            indl = -1
        if indr != 7 and corr[indr] == 0:
            possible.append(indr)
            indr += 1
        else:
            indr = 7
        if indl == -1 and indr == 7:
            break
    return possible

def check_corr2(corr, index):
    indl = index-1
    indr = index+1
    possible = [index]
    while True:
        if indl >= 0 and corr[indl] == 0:
            possible.append(indl)
            indl -= 1
        else:
            indl = -1
        if indr <= 6 and corr[indr] == 0:
            possible.append(indr)
            indr += 1
        else:
            indr = 7
        if indl == -1 and indr == 7:
            break
    poss2 = []
    if 0 in possible:
        poss2.append(1)
    if 1 in possible or 2 in possible:
        poss2.append(1)
    if 2 in possible or 3 in possible:
        poss2.append(2)
    if 3 in possible or 4 in possible:
        poss2.append(3)
    if 4 in possible or 5 in possible:
        poss2.append(4)
    if 6 in possible:
        poss2.append(4)
    return poss2

def main():
    corr = [0]*7
    #corr = [0, 0, 0, 4, 0, 0, 0]
    final = [[1,1],[2,2],[3,3],[4,4]]
    nests = [[2,4],[2,3],[4,1],[1,3]]
    #nests = [[0,1],[0,0],[0,0],[4,1]]
    #final = [[1,1],[0,0],[0,0],[4,4]]
    s = 0
    ko = []
    visited = []
    ps = possible_moves(s, corr, nests)
    for i in ps:
        heapq.heappush(ko, i)
    s, corr, nests = heapq.heappop(ko)
    while True:
        #print(corr, nests)
        visited.append([corr, nests])
        if nests == final:
            return s
        ps = possible_moves(s,corr, nests)
        for i in ps:
            heapq.heappush(ko, i)
        s, corr, nests = heapq.heappop(ko)
        while [corr, nests] in visited:
            s, corr, nests = heapq.heappop(ko)

if __name__ == '__main__':
    print(main())
    #print(possible_moves(0, [0, 0, 0, 0, 0, 0, 0], [[4, 0], [0, 0], [0, 0], [0, 0]]))