def F(n):
    fib=[0,1,1,2]
    for i in range (4, n+1):   
        fib.append(fib[i-1]+fib[i-2]-fib[i-4])

    return fib[n]
