import time
import re

def main():
    with open(r".\2023\6\input.txt") as f:
        lines = f.readlines()
    data = [[int(i) for i in re.findall(r'-?\d+', row)] for row in lines]
    print(data)
    races = [(data[0][i], data[1][i]) for i in range(len(data[0]))]
   
    mult = 1
    for race in races:
        ways = 0
        for ti in range(race[0]):
            if (race[0]-ti)*ti > race[1]:
                ways += 1
        mult *= ways
    print(mult)

    # P2
    tim = ''
    di = ''
    for i in races:
        tim += str(i[0])
        di += str(i[1])
    tim = int(tim)
    di = int(di)
    
    step = tim // 2
    done = False
    
    ss = 0

    
    curr = 0
    step = 1

    while True:
        curr += step
        ss += 1
        if (tim-curr)*curr <= di:
            step *= 10
            curr += step
        
        if (tim-curr)*curr > di:
            curr -= step
            step //= 10
            break
    
    while True:
        curr += step
        ss += 1
        if (tim-curr)*curr <= di:
            curr += step
            if step == 1 and (tim-curr)*(curr) > di:
                break
        
        if (tim-curr)*curr > di:

            curr -= step
            step //= 10
    print(curr)
    low = curr

    step = 1

    while True:
        curr += step
        ss += 1
        if (tim-curr)*curr >= di:
            step *= 10
            curr += step
        
        if (tim-curr)*curr < di:
            curr -= step
            step //= 10
            break

    while True:
        curr += step
        ss += 1
        if (tim-curr)*curr >= di:
            curr += step

        
        if (tim-curr)*curr < di:
            curr -= step
            if step == 1 and (tim-curr)*(curr) > di:
                break
            step //= 10
        print(curr)
    print(curr-low+1)
            
                

    


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
