import re



class Monkey:

    def __init__(self, data, monkeys):
        self.name = int(re.findall(r'Monkey (\d):$', data[0])[0])
        self.items = [int(i) for i in re.findall(r'(\d{2})', data[1])]
        self.op = re.findall(r'new = (old .*)$', data[2])[0]
        self.div = int(re.findall(r'(\d+)$', data[3])[0])
        self.true = int(re.findall(r'(\d+)$', data[4])[0])
        self.false = int(re.findall(r'(\d+)$', data[5])[0])
        self.monkeys = monkeys
        self.inspects = 0

    def throw(self):
        for old in self.items:
            # new = eval(self.op)//3 # p1
            new = eval(self.op)%self.mods # p2
            if new % self.div == 0: self.monkeys[self.true].items.append(new)
            else: self.monkeys[self.false].items.append(new)
            self.inspects += 1
        self.items = []


def main():
    with open(r'2022\11\input.txt', 'r') as file:
        data = file.read()
    data = data.split('\n\n')
    monkeys = []
    for i in data:
        monkeys.append(Monkey(i.splitlines(), monkeys))
    mod = 1
    for monkey in monkeys : mod *= monkey.div
    for monkey in monkeys: monkey.mods = mod
    for i in range(10000):
        for monkey in monkeys: monkey.throw()
    inspects = []
    for monkey in monkeys: inspects.append(monkey.inspects)
    inspects.sort()
    print(inspects[-1]*inspects[-2])

if __name__ == '__main__':
    main()