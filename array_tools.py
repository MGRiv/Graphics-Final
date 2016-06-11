def slice(array, n):
    out = []
    if (n > len(array[0])):
        raise IndexError ('Slice index is too big')
    for a in array:
        out.append(a[n])
    return out
