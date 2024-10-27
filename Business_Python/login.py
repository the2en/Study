# 의사코드

# 아이디/비번 딕셔너리

# 아이디를 입력한다
# 아이디가 저장된 값과 일치하면
#     비밀번호를 입력한다
#     비밀번호가 일치하면
#         로그인 성공
#     일치하지 않으면
#         로그인 실패
#         다시 비밀번호 입력
# 그렇치 않으면
#     아이디 오류
#     다시 아이디 입력

dic = {'홍길동':'1234'}

while True:
    userID = input('아이디 입력: ')

    if userID in dic:
        while True:
            passwd = input('비밀번호 입력: ')

            if passwd == dic[userID]:
                print('로그인 성공')
                break
            else:
                print('로그인 실패')
        break
    else:
        print('아이디 오류')