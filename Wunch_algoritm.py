from pprint import pprint

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
            a=x[i-1,j-1] + Score(s[i],t[j])
            b=x[i-1,j] + Score(s[i],'-')
            c=x[i,j-1] + Score('-',t[j])
            if a>=b and a>=c:
                x[i][j] = a
            if b>=a and b>=c:
                x[i][j] = b
            if c>=a and c>=b:
                x[i][j] = c
            
    pprint(x)
