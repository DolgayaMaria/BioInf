def F(DNA):
    res = []
    for letter in DNA:
        if letter == 'A':  
           res.append('T')
        if letter == 'C':
           res.append('G')
        if letter == 'T':
           res.append('A')
        if letter == 'G':
           res.append('C')
    res = res[::-1]
    
    return ''.join(res)
    
        
    
