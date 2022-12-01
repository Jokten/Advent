import numpy
import itertools
import heapq


def main():
    min_mana = 100000
    player = [50, 0, 500]
    boss = [55, 8]
    spells = {'Magic Missile': [53, 4, 0, 0, 0, 0, 0, 0, 0, 0],
                'Drain': [73, 2, 2, 0, 0, 0, 0, 0, 0, 0],
                'Shield': [113, 0, 0, 7, 6, 0, 0, 0, 0, 0],
                'Poison': [173, 0, 0, 0, 0, 6, 3, 0, 0, 0],
                'Recharge': [229, 0, 0, 0, 0, 0, 0, 5, 101, 0]}
    
    # Part 1
    
