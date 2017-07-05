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

    
    m = x[0][0]
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
            if x[i][j] < 0:
                x[i][j] = 0
            if x[i][j] > m:
                m = x[i][j]
                mi = i
                mj = j
                      


    sa=''
    ta=''
    i=mi
    j=mj
    while i != 0 or j != 0:
        if i > 0 and j > 0 and x[i][j]==x[i-1][j-1] + Score(s[i-1],t[j-1]):
            sa = s[i-1] + sa
            ta = t[j-1] + ta
            i-=1
            j-=1
        elif i>0 and x[i][j]==x[i-1][j] + Score(s[i-1],'-'):
            sa = s[i-1] + sa
            ta = '-' + ta
            i-=1                           
        elif j>0 and x[i][j]==x[i][j-1] + Score('-',t[j-1]):
            sa = '-'+sa
            ta = t[j-1] + ta
            j-=1
        elif x[i][j] == 0:
            return i
        

    #pprint(x)

    print(sa)
    print(ta)

with open('/Users/Guest/Downloads/small_ref.fa') as f:
    first = True
    ref = ''
    ref_name = ''
    for line in f:
        if first:
            ref_name = line.strip()
            first = False
            continue
        ref+=line.strip()           

with open('/Users/Guest/Downloads/output.txt', 'w') as out:
    with open('/Users/Guest/Downloads/small.fastq') as f:
        counter = 0
        for line in f:
            if counter % 4 == 0:
                rid_name = line.strip()
                counter += 1
                continue
            if counter % 4 == 1:
                rid = line.strip()
                counter += 1
                continue
            if counter % 4 == 2:
                counter += 1
                continue
            if counter % 4 == 3:
                qual = line.strip()
                counter += 1

            coordinate = align(ref, rid)
            print(rid_name,ref_name,coordinate,rid,qual,sep = '\t', file = out)
            
            

            
            

        
            
        
       
    
   

    

