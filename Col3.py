def swap_columns(a, i, j):
    for b in range(len(a)):
        a[b,i], a[b,j] = a[b,j], a[b,i]
    
    return a 
        
