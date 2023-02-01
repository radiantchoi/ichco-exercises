# 이것이 취업을 위한 코딩 테스트다 p.311 모험가 길드

n = int(input())
people = list(map(int, input().split()))

people.sort()

result = 0
party = []

for person in people:
    party.append(person)
    if person == len(party):
        party = []
        result += 1

print(result)