def main():
    with open(r".\2023\1\input.txt", "r") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]

    digits = ['0','1','2','3','4','5','6','7','8','9', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    summ = 0
    done = False
    for line in lines:
        first = 0
        for i in range(len(line)):
            for digit in digits:
                if line[i:i+len(digit)] == digit:
                    first = digits.index(digit)%10
                    done = True
                    break
            if done:
                done = False
                break
        second = 0
        for i in range(len(line)-1, -1, -1):
            for digit in digits:
                if line[i-len(digit)+1:i+1] == digit:

                    second = digits.index(digit)%10
                    done = True
                    break
            if done:
                done = False
                break

        summ += int(digits[first]+digits[second])
        

    print(summ)
if __name__ == "__main__":
    main()