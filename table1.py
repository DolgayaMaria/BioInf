from pprint import pprint

def Score(a, b):
    if a == '-' or b == '-':
        return -1

    if a == b:
        return 1
    else:
        return -1
    

def align(s,t):
    x=[]
    for i in range(0,len(s)+1):
        r=[]
        for j in range (0,len(t)+1):
            r.append(0)
        x.append(r)
    for i in range(0,len(s)+1):
        x[i][0]=-i       
    for j in range(0,len(t)+1):
        x[0][j]=-j
    
        
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            a=x[i-1][j-1] + Score(s[i-1],t[j-1])
            b=x[i-1][j] + Score(s[i-1],'-')
            c=x[i][j-1] + Score('-',t[j-1])
            if a>=b and a>=c:
                x[i][j] = a
            if b>=a and b>=c:
                x[i][j] = b
            if c>=a and c>=b:
                x[i][j] = c
            


    sa=''
    ta=''
    i=len(s)
    j=len(t)
    while i != 0 or j != 0:
        if i > 0 and j > 0 and x[i][j]==x[i-1][j-1] + Score(s[i-1],t[j-1]):
            sa = s[i-1] + sa
            ta = t[j-1] + ta
            i-=1
            j-=1
        elif i>0 and x[i][j]==x[i-1][j] + Score(s[i-1],'-'):
            sa = s[i-1] + sa
            ta = '-' +ta
            i-=1                           
        elif j>0 and x[i][j]==x[i][j-1] + Score('-',t[j-1]):
            sa = '-'+sa
            ta = t[j-1] + ta
            j-=1

    print(sa)
    print(ta)








    
