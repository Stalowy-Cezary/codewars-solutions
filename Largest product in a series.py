def greatest_product(n):
    a = [int(x) for x in n]
    z = 0
    for i in range(len(a)-4):
        if a[i]*a[i+1]*a[i+2]*a[i+3]*a[i+4] > z:
            z = a[i]*a[i+1]*a[i+2]*a[i+3]*a[i+4]
    return z
