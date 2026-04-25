def solution(my_string):
    O = []
    result = ''
    for i in my_string:
        if i not in O:
            O.append(i)
            result += i
    return result
