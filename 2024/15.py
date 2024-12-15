import aoc, time, os

def move(pos,dir,boxes, walls):
    if pos+dir in boxes:
        return move(pos+dir,dir, boxes, walls)
    elif pos+dir in walls: return 0
    else:
        boxes.add(pos+dir)
        return 1
    
def move2(box,dir,boxes, walls):
    if (box[0]+2*dir, box[1]+2*dir) in boxes:
        if move2((box[0]+2*dir, box[1]+2*dir),dir, boxes, walls):
            boxes.remove(box)
            boxes.add((box[0]+dir, box[1]+dir))    
            return 1
    elif box[0]+2*dir in walls and box[1]+2*dir in walls: return 0
    else:
        boxes.remove(box)
        boxes.add((box[0]+dir, box[1]+dir))
        return 1

def check_move2(box, dir, boxes, walls, move):
    bright = box[0]+dir+1j, box[1]+dir+1j
    bleft = box[0]+dir-1j, box[1]+dir-1j
    bnext = box[0]+dir, box[1]+dir
    if box[0]+dir in walls or box[1]+dir in walls: return 0

    elif bnext in boxes:
        if check_move2(bnext, dir, boxes, walls, move):
            if move:
                boxes.remove(box)
                boxes.add(bnext)
            return 1
        return 0
        
    elif bleft in boxes or bright in boxes:
        ok1 = bleft not in boxes or check_move2(bleft, dir, boxes, walls, move)
        ok2 = bright not in boxes or check_move2(bright, dir, boxes, walls, move)
        if ok1 and ok2:
            if move: 
                boxes.remove(box)
                boxes.add(bnext)
            return 1

    else:
        if move:
            boxes.remove(box)
            boxes.add(bnext)
        return 1
    
def plot(boxes,walls, size, pos, p):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for Windows ('cls') or Unix/Linux ('clear')
    room = [['.' for i in range(size*(1+p))] for j in range(size)]
    for b in boxes:
        if type(b) == tuple:
            room[int(b[0].real)][int(b[0].imag)] = "["
            room[int(b[1].real)][int(b[1].imag)] = "]"
        else: room[int(b.real)][int(b.imag)] = "O"
    for w in walls: room[int(w.real)][int(w.imag)] = "#"
    room[int(pos.real)][int(pos.imag)] = "@"
    for i in room: print("".join(i))

data = aoc.get_data(2024,15).split("\n\n")
walls, boxes = set(), set()
for e, i in enumerate(data[0].split("\n")):
    for e1, j in enumerate(i):
        if j == "#": walls.add(e+1j*e1)
        elif j == "O": boxes.add(e+1j*e1)
        elif j == "@": orgpos = e+1j*e1
inst = list(data[1])
pos = orgpos

dirs = {"^": -1, "<": -1j, ">": 1j, "v": 1}

walls2, boxes2 = set(), set()
for i in walls:
    walls2.add(int(i.imag)*1j+i)
    walls2.add(int(i.imag)*1j+i+1j)

for i in boxes:
    boxes2.add((int(i.imag)*1j+i, int(i.imag)*1j+i+1j))

for d in inst:
    if d not in dirs: continue
    dir = dirs[d]
    if pos+dir in walls: continue
    if pos+dir in boxes:
        if move(pos+dir, dir, boxes, walls):
            boxes.remove(pos+dir)
            pos += dir
    else:
        pos += dir

s = 0
for i in boxes:
    s+= int(i.real)*100 + int(i.imag)
print(s)

pos = orgpos + int(orgpos.imag)*1j
for d in inst:
    if d not in dirs: continue
    dir = dirs[d]
    if pos+dir in walls2: continue
    
    if dir in [1, -1]:
        l = (pos+dir-1j, pos+dir)
        r = (pos+dir, pos+dir+1j)
        if l in boxes2:
            if check_move2(l, dir, boxes2, walls2, 0):
                check_move2(l, dir, boxes2, walls2, 1)
                pos += dir
        elif r in boxes2:
            if check_move2(r, dir, boxes2, walls2, 0):
                check_move2(r, dir, boxes2, walls2, 1)
                pos += dir
        else: pos += dir

    else:
        if (pos+dir, pos+dir*2) in boxes2:
            if move2((pos+dir, pos+dir*2), dir, boxes2, walls2): pos += dir
        elif (pos+dir*2, pos+dir) in boxes2:

            if move2((pos+dir*2, pos+dir), dir, boxes2, walls2): pos += dir
        else:
            pos += dir
    #plot(boxes2, walls2, len(data[0].split("\n")), pos, 1)
    #time.sleep(0.01)

s = 0
for i in boxes2:
    s+= int(i[0].real)*100 + int(i[0].imag)
print(s)
