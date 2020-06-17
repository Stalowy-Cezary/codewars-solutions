def get_sum(a,b):
    if a>b:
        lista = range(b,a+1)
        return sum(lista)
    elif b>a:
        lista = range(a,b+1)
        return sum(lista)
    else:
        return a
