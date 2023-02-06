# 이것이 취업을 위한 코딩테스트다 p.321 럭키 스트레이트
# https://www.acmicpc.net/problem/18406

number = input()

front = 0
back = 0
border = len(number) // 2

for i in range(len(number)):
    piece = int(number[i])
    
    if i < border:
        front += piece
    else:
        back += piece

if front == back:
    print("LUCKY")
else:
    print("READY")