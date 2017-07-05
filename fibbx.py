def F(n,m):
    fib=[1, 1]
    for i in range (2, n+1):
        # print(fib)
        if i > m:
            fib.append(fib[i-1]+fib[i-2]-fib[i-m-1])
        elif i == m:
            fib.append(fib[i-1]+fib[i-2] - 1)
        else: 
            fib.append(fib[i-1]+fib[i-2])

    return fib[n-1]

# print(F(5, 3))
3
for i in range(1, 9):
    print(F(i, 3))
            


