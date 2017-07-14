def extract_kmers(read, k):
    res = []

    for i in range(0,len(read)-k+1):
        res.append(read[i:i+k])
    
            
    return res
