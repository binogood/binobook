
# 이진 탐색 알고리즘
# 정렬된 리스트에서 절반씩 탐색

def linear_search(element, some_list):
    start_idx = 0 
    end_idx = len(some_list) - 1
    while start_idx <= end_idx:
        mid_idx = (end_idx + start_idx) // 2
        if some_list[mid_idx] == element:
            return mid_idx
        elif some_list[mid_idx] > element:
            end_idx = mid_idx - 1
        else:
            start_idx = mid_idx + 1

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))

