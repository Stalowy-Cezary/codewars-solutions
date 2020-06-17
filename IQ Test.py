def iq_test(n):
    u = [int(x) for x in n.split()]
    even = [x for x in u if x % 2 == 0]
    odd = [x for x in u if x % 2 != 0]
    if len(even) > len(odd):
        return u.index(odd[0])+1
    else:
        return u.index(even[0])+1
