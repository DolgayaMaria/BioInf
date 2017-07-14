a = [1,0,3,7,-5,30,61,17,42]
visited = []
for i in range(len(a)):
    visited.append(False)
lists = {0:[4,8], 1:[7], 2:[4,5,7], 3:[2], 4:[0,2], 5:[2,7], 6:[], 7:[1,5], 8:[0,2]}
stack = [0]
m = 0
mi = 0
while stack:
    current_v = stack.pop()
    print(current_v)
    visited[current_v] = True
    neighbours = lists[current_v]
    for neighbour in neighbours:
        if (neighbour not in stack) and (visited[neighbour] == False):
            stack.append(neighbour)
    if a[current_v] > m:
        m = a[current_v]
        mi = current_v
print(m,mi)
    
    


    
