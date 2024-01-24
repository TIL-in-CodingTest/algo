import sys
from collections import deque

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

node, line = map(int, input().split())
graph = [[] for _ in range(node+1)]

for _ in range (line) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (node+1)
count = 0

def dfs(start) :
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)


for i in range(1, node+1):
    if visited[i] == False:
        count += 1
        dfs(i)

print(count)