import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# collections Module
# 파이썬의 범용 내장 컨테이너 dict, list, set, tuple에 대한 대안을 제공하는 특수 컨테이너
# 데이터형을 구현

# Counter = 해시 가능한 객체를 세는 데 사용하는 딕셔너리 서브 클래스