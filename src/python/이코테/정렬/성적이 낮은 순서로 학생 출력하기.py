n = int(input())
info = []

for _ in range (n):
    tmp = input().split()
    info.append((tmp[0], int(tmp[1])))
    print(info)

info = sorted(info, key = lambda student: student[1])

for i in info:
    print(i[0], end=' ')