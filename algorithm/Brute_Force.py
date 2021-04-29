def max_product(left_cards, right_cards):
    result = -1
    
    for i in left_cards:
        for j in right_cards:
            result = max(result, i * j)
    return result
    
# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6])

# Brute Force를 사용한 가까운 매장 찾기
# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    result = []
    dist = distance(coordinates[0],coordinates[1])
    for i in range(len(coordinates)) :
        for j in range(i + 1,len(coordinates)):
            if dist > distance(coordinates[i], coordinates[j]):
                dist = distance(coordinates[i], coordinates[j])
                result = [coordinates[i],coordinates[j]]
    return result
            
# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))


# Burte Force 강남역 폭우 

def trapping_rain(buildings):
    total_height = 0

    # 리스트의 각 인덱스을 돌면서 해당 칸에 담기는 빗물의 양을 구한다
    # 0번 인덱스와 마지막 인덱스는 볼 필요 없다
    for i in range(1, len(buildings) - 1):
        # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구한다
        max_left = max(buildings[:i])
        print(f"나는 max_left{max_left}")
        max_right = max(buildings[i:])
        print(f"나는 max_right{max_right}")

        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(max_left, max_right)
        print(f"나는 upper_bound{upper_bound}")

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        total_height += max(0, upper_bound - buildings[i])
        print(f"나는 total_height {total_height}")

    return total_height

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))