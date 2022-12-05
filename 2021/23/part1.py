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

def free_nest(num, nests):
    top = -1
    l = len(nests[0])
    for i in range(l):
        if nests[num-1][i] == 0:
            top = i
    if top == l-1:
        return top
    elif top == -1: return -1
    else:
        if nests[num-1][top+1:] == [num]*(l-top-1):
            return top
        else: return -1

def from_nest(num, nests):
    top = -1
    l = len(nests[0])
    for i in range(l):
        if nests[num][i] != 0:
            top = i
            break
    if top == -1:
        return -1
    elif top == l-1 and nests[num][top] != num+1:
        return top
    elif nests[top] != num+1:
        return top
    elif nests[top+1:] != [num+1]*(l-top-1):
        return top
    else: return -1

def possible_moves(cs, corr, nests):
    moves = []
    for e, i in enumerate(nests):
        ind = from_nest(e, nests)
        if ind != -1:
            possible = check_corr(corr, e)
            for j in possible:
                new_nest = copy.deepcopy(nests)
                new_nest[e][ind] = 0
                new_corr = copy.deepcopy(corr)
                new_corr[j] = i[ind]
                cos = cost[i[ind]]
                s = ind*cos + cos*2*(int(abs(e+1.5-j))+1)
                if j in [0, 6]:
                    s -= cos
                moves.append((cs+s, new_corr, new_nest))

    for e, i in enumerate(corr):
        top = -1
        if i != 0:
            top = free_nest(i, nests)
        if top != -1:
            pos2 = check_corr2(corr, e)
            if i in pos2:
                new_nest = copy.deepcopy(nests)
                new_nest[i-1][top] = i
                new_corr = copy.deepcopy(corr)
                new_corr[e] = 0
                cos = cost[i]
                s = top*cos + cos*2*(int(abs(e-0.5-i))+1)
                if e in [0, 6]:
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
    if 1 in possible or 2 in possible:
        poss2.append(1)
    if 2 in possible or 3 in possible:
        poss2.append(2)
    if 3 in possible or 4 in possible:
        poss2.append(3)
    if 4 in possible or 5 in possible:
        poss2.append(4)
    return poss2

def main():
    corr = [0]*7
    final = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
    nests = [[2,4,4,4],[2,3,2,3],[4,2,1,1],[1,1,3,3]]

    s = 0
    ko = []
    visited = set()
    ps = possible_moves(s, corr, nests)
    for i in ps:
        heapq.heappush(ko, i)
    s, corr, nests = heapq.heappop(ko)
    cn = 1
    while True:
        cn+=1
        #print(corr, nests)
        visited.add(tuple(flatten([corr, nests])))
        if nests == final:
            return s
        ps = possible_moves(s,corr, nests)


        for i in ps:
            heapq.heappush(ko, i)
        s, corr, nests = heapq.heappop(ko)
        while tuple(flatten([corr, nests])) in visited:
            s, corr, nests = heapq.heappop(ko)


if __name__ == '__main__':
    print(main())