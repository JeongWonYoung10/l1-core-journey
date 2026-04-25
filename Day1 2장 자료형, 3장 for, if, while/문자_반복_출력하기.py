def solution(my_string, n):
    parts = []
    for i in my_string:
        parts.append(i * n)
        
    return "".join(parts)  
