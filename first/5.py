# 이것이 취업을 위한 코딩 테스트다 p.315 볼링공 고르기

from itertools import combinations

n, m = map(int, input().split())
balls = list(map(int, input().split()))

cases = list(filter(lambda x: x[0] != x[1], list(combinations(balls, 2))))
print(len(cases))

# 파이썬 고차함수도 잘 활용해보자.