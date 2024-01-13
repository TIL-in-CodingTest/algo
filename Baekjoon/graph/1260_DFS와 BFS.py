from collections import deque

node, line, v = map(int, input().split())
graph = [[] for _ in range(node + 1)]

for i in range(line) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range (node+1):
    graph[i].sort()

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True
            
## 각 함수 호출하기 전에 visited 초기화해주기!!!!!
visited=[False] * (node+1)
dfs(graph, v, visited)
print()
visited = [False] * (node + 1)
bfs(graph, v, visited)
