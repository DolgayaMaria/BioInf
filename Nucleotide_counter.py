def F(seq):
    res = {}
    for letter in seq:
        if letter not in 'ACGT':
            print('Wrong string')
            return {}
        if letter in res:
            res[letter] += 1
        else:
            res[letter] = 1
        
    return res

        
            
        
            
        
    
