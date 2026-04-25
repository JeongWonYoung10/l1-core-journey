def solution(s):
    O = []
    for i in s:
        if s.count(i) == 1:
            O.append(i)
    O.sort()
    return "".join(O)
