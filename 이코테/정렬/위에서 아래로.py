n = int(input())
link = [int(input()) for _ in range(n)]

link.sort(reverse=True)

for i in range (len(link)):
    print(link[i], end=' ')