import re

def data_loader(year,day,two_parts=False):
    with open(f'{year}\\{day}\input.txt', 'r') as file:
        data = file.read()
    if two_parts:
        return [i.splitlines() for i in data.split('\n\n')]
    else:
        return data.splitlines()

def parse_numbers(data):
    return [[int(i) for i in re.findall(r'-?\d+', row)] for row in data]