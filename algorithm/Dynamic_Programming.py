# Dynamic Programmming 
# 한 번 계산한 결과를 재활용하는 방식

# Optimal Substructure (최적 부분 구조)
# Overlapping Substructure (중복되는 부분 문제)
# Memoization - 중복되는 계산은 한 번만 계산 후 메모


# 피보나치 수열 Memoization 1

def fib(n):
    fib_cache = {1:1, 2:1}
    if n > 2:
        for i in range(3, n+1):
            fib_cache[i]=fib_cache[i-2]+fib_cache[i-1]
    return fib_cache[n]

# 테스트
print(fib(10))
print(fib(50))
print(fib(100))


# 피보나치 수열 Memoization 2

def fib_memo(n, cache):
    if n < 3:
        return 1
    if n in cache:
        return cache[n]
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]

def fib(n):
    fib_cache = {}
    return fib_memo(n, fib_cache)

# 테스트
print(fib(10))
print(fib(50))
print(fib(100))



# 피보나치 수열 공간 최적화

def fib_optimized(n):

    current = previous = 1
    
    for i in range(1, n-1) :
        
        current = previous + current
        previous = current - previous

    return current