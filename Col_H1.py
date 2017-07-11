def F(n):
    n = n.split()
    n.sort()
    maximum = 0
    counter = 1
    word = ''
    for i in range(1, len(n)):
        if n[i-1] == n[i]:
            counter += 1
        else:
            if maximum < counter:
                maximum = counter
                word = n[i-1]
            counter = 1
    return word
        
        
        
