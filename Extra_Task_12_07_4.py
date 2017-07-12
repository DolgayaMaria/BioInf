def F(n, lists):
    res = ''
    for string in range(len(lists)-1):
        res += lists[string][:-n]
    res += lists[-1]
        

    return res
    
