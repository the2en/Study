# 의사코드

# 랜덤 모듈 불러오기

# 랜덤 사칙연산 함수(첫 번째 숫자, 두 번째 숫자)
#     1~4 사이의 난수 생성
#     1일 때
#         정답 = 첫 번째 숫자 + 두 번째 숫자
#         기호 = '+'
#     2일 때
#         정답 = 첫 번째 숫자 - 두 번째 숫자
#         기호 = '-'
#     3일 때
#         정답 = 첫 번째 숫자 * 두 번째 숫자
#         기호 = '*'
#     나머지(= 4일 때)
#         정답 = 첫 번째 숫자 / 두 번째 숫자
#         기호 = '/'
#     정답, 기호 반환

# '사칙연산 공부를 해봅시다!' 출력

# count = 0으로 초기화

# 반복
#    숫자1 = 1부터 100 미만의 난수
#    숫자2 = 1에서 100 미만의 난수
#    랜덤 사칙연산 함수에 숫자1과 숫자2를 입력하여 정답과 기호 값을 받는다
#    숫자1, 기호, 숫자2 로 이루어진 문제 출력 > 답 입력
#    답이 '종료'면
#        프로그램 종료
#    그 외의 경우면
#        답이 정답과 동일할 때
#            count 1회 추가
#            '잘했어요!' 출력
#        답이 틀렸을 때
#            '틀렸어요. 하지만 다음 번에는 잘할 수 있죠?' 출력
#            프로그램 종료

# 최종적으로 맞힌 문제의 개수 출력


import random as rd

def randNum(n1, n2):                    # 랜덤 사칙연산을 randNum 함수로 정의함
    randnum = rd.randrange(1, 5)

    if randnum == 1:
        a = n1 + n2
        e = '+'
    elif randnum == 2:
        a = n1 - n2
        e = '-'
    elif randnum == 3:
        a = n1 * n2
        e = '*'
    else:
        a = n1 / n2
        e = '/'
    return a, e                         # randNum 함수를 통해 a(=정답)과 e(=사칙연산 기호)를 반환

print('사칙연산 공부를 해봅시다!')

count = 0

while True:
    num1 = rd.randrange(1, 100)
    num2 = rd.randrange(1, 100)

    ans1, emo = randNum(num1, num2)

    print(num1, emo, num2, end=" ")    # 문제 생성
    ans2 = input('= ')                 # 정답 입력

    if ans2 == '종료':                  # 종료 입력시 프로그램 종료
        break
    else:
        if ans1 == float(ans2):        # 나눗셈의 경우 정답이 실수일 수 있으므로 int가 아닌 float
            count += 1                 # 맞힌 횟수 추가
            print('잘했어요!!')
        else:
            print('틀렸어요. 하지만 다음 번에는 잘할 수 있죠?')
            break

print('총 맞힌 문제의 수 =', count)