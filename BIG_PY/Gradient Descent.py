# 경사하강법
# 1차 근삿값 발견용 최적화 알고리즘
# 함수의 기울기(경사)를 구하고 경사의 반대 방향으로 계속 이동시켜 극값에 이를 때까지 반복시키는 것
# 최솟값 찾는 방법

x = 4
learning_rate = 0.1

count = 0         # 반복 횟수 세기

while True:
    y = x ** 2
    print(f'x값 갱신 횟수: {count}번, y 값: {y}')

    if y <= 0.1:
        break
    else:
        x = x - learning_rate * (2 * x)
        count += 1