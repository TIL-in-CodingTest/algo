n = int(input())
data = list(map(int, input().split()))
data.sort() # 정렬 하려면 list로 변환해준다음에 써야함
x = 0
y = 0

for i in data:
    x += i 
    y += x

print(y)
