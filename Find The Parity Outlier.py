def find_outlier(integers):
    even = []
    odd = []
    for i in integers:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(odd) and len(even) > 0:
        if len(odd) > len(even):
            return even[0]
        else:
            return odd[0]
