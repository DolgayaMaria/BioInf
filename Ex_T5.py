def F(a):
    a = a.split(', ')
    b = []
    c = []
    for i in range(len(a)):
        b += a[i].split()
        
    for i in range (0, len(b), 2):
        c += [b[i]] * int(b[i + 1])
    c.sort()
    return ', '.join(c)
