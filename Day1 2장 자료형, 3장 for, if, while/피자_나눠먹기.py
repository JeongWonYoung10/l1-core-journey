def solution(slice, n):
    pizzas = n // slice
    if n % slice != 0:
        pizzas = pizzas + 1
    return pizzas
    
