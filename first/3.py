# 이것이 취업을 위한 코딩 테스트다 p.313 문자열 뒤집기

s = input()

zeroes = 0
ones = 0
prev = s[0]

if len(s) > 1:
    for i in range(1, len(s)):
        current = s[i]
        if prev != current:
            if current == "0":
                zeroes += 1
            else:
                ones += 1
            
        prev = current

print(min(zeroes, ones))