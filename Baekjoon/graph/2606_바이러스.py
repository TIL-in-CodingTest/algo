from collections import deque

node = int(input())
line = int(input())

visited = [False]*(node+1)
graph=[[] for _ in range (node+1)]
ctn = 0

for i in range (line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start, visited):
    ctn = 0
    queue = deque([start])
    visited[start] = True
    while queue :
        v = queue.popleft()
        visited[v] = True
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                bfs(graph, i, visited)

bfs(graph, 1, visited)

for i in range(node+1):
    if visited[i] == True :
        ctn += 1
print(ctn-1)
