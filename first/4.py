# 이것이 취업을 위한 코딩 테스트다 p.314 만들 수 없는 금액

from itertools import combinations

n = int(input())
coins = list(map(int, input().split()))

cases = set()

for i in range(1, n+1):
    case = set(combinations(coins, i))
    cases = cases | case

prices = list(set(list(map(sum, cases))))

result = 1
while result <= prices[-1]:
    if result not in prices:
        break

    result += 1

print(result)

# O(n^2) 풀이법인데, 더 좋은 방법이 있을 것 같다.
# 하지만 일단 동전 갯수가 최대 1000개이므로 이 알고리즘으로도 정답은 낼 수 있다.