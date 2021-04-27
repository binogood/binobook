# 재귀 함수 (Recursion)

# 피보나치 수열
def fib(n):
    if n == 0:
        return 0
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)

for i in range(1, 11):
    print(fib(i))


# 삼각수

def triangle_number(n):
    if n == 0:
        return 0
    return 1 if n < 2 else triangle_number(n - 1) + n

for i in range(1, 11):
    print(triangle_number(i))


# 자릿수 합

def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))

# 리스트 뒤집기

def flip(some_list):
    return some_list if len(some_list) == 0 or len(some_list) == 1 else some_list[-1:] + flip(some_list[:-1])

some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)

# 이진 탐색 재귀
def binary_search(element, some_list, start_index=0, end_index=None):
    if end_index == None:
        end_index = len(some_list)

    if start_index > end_index:
        return None

    mid_index = (start_index + end_index) // 2

    if some_list[mid_index] == element:
        return mid_index

    if element < some_list[mid_index]:
        return binary_search(element, end_index, start_index, mid_index - 1)

    else: 
        binary_search(element, some_list, mid_index + 1, end_index)