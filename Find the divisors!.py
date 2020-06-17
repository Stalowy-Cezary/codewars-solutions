def divisors(integer):
    lista = []
    for i in range(2,integer):
        if integer%i==0:
            lista.append(i)
    if not lista:
        integer =str(integer)
        return '{} is prime'.format(integer)
    else:
        return lista
