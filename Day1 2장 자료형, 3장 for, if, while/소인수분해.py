def solution(n):
    primes = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            primes.append(d)
            while n % d == 0:
                n //= d
        d = d + 1
    if n > 1:
        primes.append(n)
    return primes
        
            
