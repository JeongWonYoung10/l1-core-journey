def solution(my_string):
    t = 0
    for i in my_string:
        if i in "123456789":
            t += int(i)
    return t
                
