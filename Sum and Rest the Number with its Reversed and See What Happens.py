def sum_dif_rev(n):
    lista = []
    for i in range (45,2000000):
        a = i+int(str(i)[::-1])
        b = (abs(i-int(str(i)[::-1])))
        if b != 0:
            if a%b == 0 and i%10 != 0:
                lista.append(i)
                if len(lista) == n:
                    return lista[n-1] 
