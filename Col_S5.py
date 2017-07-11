def one(n):
    tabl = []
    for i in range(n):
        tabl.append([])
        for j in range(n):
            if i == j:
                tabl[i].append(1)
            else:
                tabl[i].append(0)
    return tabl

    
