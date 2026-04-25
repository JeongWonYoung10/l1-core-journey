def solution(order):
    p = 0
    for i in str(order):
        if i in "369":
            p += 1
    return p
