
# 선형 탐색 알고리즘 
# 처음 부터 하나씩 확인

def linear_search(element, some_list):
    for idx in some_list:
        if idx == element:
            return some_list.index(element)
    return None


print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))