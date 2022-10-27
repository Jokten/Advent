import hashlib
if __name__ == '__main__':
    input = 'iwrupvqb'
    done = 0
    test = 'abcdef'
    print(hashlib.md5('abcdef609043'.encode()).hexdigest())
    cur = 0
    while done == 0:
        cur += 1
        hash = input+str(cur)
        result=hashlib.md5(hash.encode()).hexdigest()
        if result.startswith('000000'):
            done = 1
    print(cur)
