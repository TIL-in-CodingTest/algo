def solution(array, commands):
    answer = []
    for x in commands :
        i, j, k = x
        answer.append(sorted(array[i-1:j])[k-1])
    return answer