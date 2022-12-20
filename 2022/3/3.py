import numpy as np
import itertools

st = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def load_data():
    with open("2022\\3\\input.txt", "r") as f:
        data = f.read().splitlines()
    return data

def part1(data):
    return sum(st.index(list(set(i[:len(i)//2]) & set(i[len(i)//2:]))[0])+1 for i in data)

def part2(data):
    return sum(st.index(list(set(data[i]) & set(data[i+1]) & set(data[i+2]))[0])+1 for i in range(0,len(data),3))

def main():
    d = load_data()
    print(part1(d))
    print(part2(d))

if __name__ == "__main__":
    main()