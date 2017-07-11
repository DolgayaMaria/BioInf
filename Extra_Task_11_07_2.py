def F(lists):
    res = []
    
    for number in range(1,len(lists)//2 + 1):
        res.append((lists[number - 1], lists[-number]))
        
   
    return res    
