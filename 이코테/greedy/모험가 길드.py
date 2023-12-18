# 현재 그룹에 포함된 모험가 수 >= 현재 확인 공포도 -> 그룹으로 설정

n = int(input())
data = map(int, input().split())
data.sort()

count = 0 # 현재 그룹에 포함된 모험가 수
group = 0 # 총 그룹 수

for i in range(count):
    if data[i] < data[i+1]:
        group += 1

for i in data :
    count += 1 #현재 그룹에 해당 모험가 포함시키기
    if count >= i : # 현재 그룹에 포함된 모험가 수 >= 현재 확인 공포도 이면 그룹 지정
        group += 1 # 총 그룹 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화
        
print(group)