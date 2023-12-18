
N = int(input())
move = input().split()

x = 1
y = 1

direction = ['L', 'R', 'U', 'D']
dy = [-1, +1, 0, 0]
dx = [0, 0, -1, +1]

for i in move :
    for j in range (4):
        if direction[j] == i :
            nx = x + dx[j]
            ny = y + dy[j]

    # 공간 벗어날 경우 무시
    if nx < 1 or ny < 1 or nx > N or ny > N :
        continue
    # 이동
    x, y = nx, ny    

print(x, y)