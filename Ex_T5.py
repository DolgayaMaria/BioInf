a = 'a 3, h 7, c 14, m 6'
a = a.split(', ')
b = []
c = []
for i in range(len(a)):
    b += a[i].split()
    
for i in range (len(b), 2):
    c += [b[i]] * int(b[i + 1])
    print(c)
c.sort()
print(', '.join(c))
