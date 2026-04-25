def solution(s1, s2):
    answer = 0
    p = 0
    for i in s1:
        for j in s2:
            if i == j:
                p = p+1
    answer = p
    return answer
