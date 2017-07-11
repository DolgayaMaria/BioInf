with open ('input.txt') as f:
    for line in f:
        line = line.strip().strip()    
    m = 0
    if m < int(line[1]):
        m = int(line[1])

    return m
