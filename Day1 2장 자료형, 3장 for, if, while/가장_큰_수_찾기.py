def solution(array):
    number = array[0]
    for i in array:
        if number >= i:
            number = number
        else: number = i
    
    answer = [number, array.index(number)]
    return answer
