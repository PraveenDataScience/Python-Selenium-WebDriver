def range(start, end, step):
    cur = start
    while cur > end:
        yield cur
        cur += step

print(range(10,20,1))