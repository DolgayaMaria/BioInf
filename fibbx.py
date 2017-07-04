def F(n,m):
    fib=[0,1]
    for i in range (2, n+1):
        if i > m:
            fib.append(fib[i-1]+fib[i-2]-fib[i-m-1])
        else: 
            fib.append(fib[i-1]+fib[i-2])

    return fib[n]
            


