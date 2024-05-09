cnt = int(input())
my_list = list(int(input()) for _ in range(cnt))

sorted_list = sorted(my_list)

for i in range(cnt):
    print(sorted_list[i])