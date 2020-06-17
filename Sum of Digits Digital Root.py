def digital_root(n):
    while n>9:
     n = [int(x) for x in str(n)]
     n = sum(n)
    return n
