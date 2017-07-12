def F(n):
    res = []
    
    for symbol in range(n*2 + 1):
        res.append(None)
        
    for symbol in range(n*2 + 1):
        if symbol % 2 == 0: 
            res[symbol] = ' ---'*n+' '
        else:
            res[symbol] = '|   '*n+'|'
            
    for symbol_1 in res:
        print(symbol_1)

    
