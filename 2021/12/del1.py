import numpy as np
import copy


class Node:
    def __init__(self):
        self.paths = []

    def add_path(self, node):
        self.paths.append(node)


def pathfinder(route, nodes, twice):
    nr = 0
    for i in nodes[route[-1]].paths:
        new_twice = twice
        if ((i not in route or twice == 0) or i.isupper()) and i not in ['end', 'start']:
            if i in route and i.islower():
                new_twice = 1
            new_route = route.copy() + [i]
            nr += pathfinder(new_route, nodes, new_twice)
        elif i == 'end':
            print(route+ ['end'],twice)

            nr += 1
    return nr


def main():
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
    routes = [i.split('-') for i in data]
    nodes = {}

    for i in routes:
        nodes.setdefault(i[0], Node())
        nodes.setdefault(i[1], Node())
        nodes[i[0]].add_path(i[1])
        nodes[i[1]].add_path(i[0])
    start_route = ['start']
    twice = 0
    print(pathfinder(start_route, nodes, twice))

if __name__ == '__main__':
    main()