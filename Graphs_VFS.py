from collections import deque

a = [1,0,3,7,-5,30,61,17,42]
added_in_queue = []
for i in range(len(a)):
    added_in_queue.append(False)
lists = {0:[4,8], 1:[7], 2:[4,5,7], 3:[2], 4:[0,2], 5:[2,7], 6:[], 7:[1,5], 8:[0,2]}
queue = deque([0])
m = 0
mi = 0
while queue:
    current_v = queue.popleft()
    print(current_v)
    neighbours = lists[current_v]
    for neighbour in neighbours:
        if  (added_in_queue[neighbour] == False):
            queue.append(neighbour)
            added_in_queue[neighbour] = True
    if a[current_v] > m:
        m = a[current_v]
        mi = current_v
print(m,mi)
    
