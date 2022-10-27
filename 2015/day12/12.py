import numpy as np
import json
if __name__ == '__main__':
    with open('day12\input.json') as f:
        data = json.load(f)
    print(data)
    def count(dat):
        coun = 0
        for i in dat:
            if type(i) is int:
                coun += i
            elif type(i) is list:
                coun += count(i)
            elif type(i) is dict and 'red' not in i.values():
                coun += count(i.values())
        return coun
    print(count(data))