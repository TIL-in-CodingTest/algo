from collections import deque

k = int(input())

queue = deque([])

for i in range(k):
    x = int(input())
    if (x == 0):
        queue.pop()
        
    else :
        queue.append(x)
        

print(sum(queue))
