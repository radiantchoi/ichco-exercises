# 이것이 취업을 위한 코딩 테스트다 p.322 문자열 재정렬

s = input()

letters = []
numbers = 0
for i in range(len(s)):
    if 64 < ord(s[i]) < 91:
        letters.append(s[i])
    else:
        numbers += int(s[i])

result = "".join(sorted(letters)) + str(numbers)
print(result)

# 오늘의 포인트는 아스키 코드.
# ord와 chr로 숫자와 숫자에 해당하는 문자를 불러올 수 있다.
# 대문자는 65~90, 소문자는 97~112이다.