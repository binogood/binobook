# 분할 정복

# 1부터 n까지의 합
def consecutive_sum(start, end):
    
    center = (start + end) // 2
    if start == end:
        return start
    return consecutive_sum(start, center) + consecutive_sum(center + 1, end)

# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))


# Divide and conquer를 활용한 합병정렬
def merge(list1, list2):
    i = 0
    j = 0

    merged_list = []

    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1
            
    if i == len(list1):
        merged_list += list2[j:]

    # list1에 남은 항목이 있으면 정렬 리스트에 추가
    elif j == len(list2):
        merged_list += list1[i:]

    return merged_list
# 합병 정렬
def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list


# Partition 함수 구현하기
# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
        
# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    j = start
    for i in range(start, end):
        if my_list[i] < my_list[end]:
            swap_elements(my_list, i, j)
            j += 1
    swap_elements(my_list, j, end)
    return j

# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)


# 퀵 정렬 구현하기

# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
        
# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    j = start
    for i in range(start, end):
        if my_list[i] < my_list[end]:
            swap_elements(my_list, i, j)
            j += 1
    swap_elements(my_list, j, end)
    return j

# 퀵 정렬
def quicksort(my_list, start, end):
    if end - start < 1:
        return 
    pivot = partition(my_list, start, end)
    quicksort(my_list, start, pivot - 1)
    quicksort(my_list, pivot + 1, end)
