def solution(s):
    p = s.split()
    q = 0
    r = 0
    for i in p:
        if i == "Z":
            q -= r
        else:
            q += int(i)
            r = int(i)
    return q
