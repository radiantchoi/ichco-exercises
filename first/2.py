# 이것이 취업을 위한 코딩 테스트다 p.312 곱하기 혹은 더하기

number = input()

result = 0
for i in range(len(number)):
    digit = int(number[i])
    if digit == 0 or result == 0:
        result += digit
    else:
        result *= digit

print(result)