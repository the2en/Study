score = 0

while True:
    question = input("다음 라운드는 상황 판단 설문입니다. 계속 진행하시겠습니까? (Y/N) >>>  ")

    if question == 'N' or question == 'n':
        JP_mbti_result = 'P'
        print("J와 P 판별 테스트가 끝났습니다. 수고하셨습니다")
        break

    elif question == 'Y' or question == 'y':
        print("MBTI J/P를 판별하기 위한 상황 판단 설문을 시작하겠습니다.")
        print("\n종강 후, 당신은 친구와 제주도로 3박 4일 여행을 떠나기로 했습니다.")
        print("그렇다면 당신은 언제부터 짐을 싸기 시작할 것인가요?")
        first = input("\nㄱ. 당연히 일주일 전부터 뭘 챙길지 고민해야지~  ㄴ. 전날이면 충분한 거 아님?   ")

        if first == 'ㄱ':
            score += 1

        print("\n드디어 떠나는 날, 비행기 시간보다 일찍 도착한 당신과 친구, 비행기 타기 전까지 무엇을 할 것인가요?")
        second = input("ㄱ. 공항 주변을 둘러 본다  ㄴ. 둘러보다 늦을 수 있으니 공항에 있는다   ")

        if second == 'ㄴ':
            score += 1

        print("\n비행기가 생각보다 일찍 도착했다. 숙소 체크인까지 남은 시간은 3시간. 당신은 무엇을 할 것인가요?")
        third = input("ㄱ. 숙소까지 걸리는 시간을 보고, 주변 맛집이나 카페를 검색해본다.  ㄴ. 일단 공항에서 벗어나고, 길가를 걷다가 끌리는 곳에 들어간다.   ")

        if third == 'ㄱ':
            score += 1

        print("\n이럴수가...봐둔 맛집이 문을 닫았다...이때 당신의 행동은?")
        four = input("ㄱ. 일단 주변을 걸으면서 생각을 해본다.  ㄴ. 이미 B안으로 갈 곳을 정해놓았다   ")

        if four == 'ㄴ':
            score += 1

        print("\n배도 채웠다...이제 야경 명소만 가면 되는데..너무 힘들다고 내일 가자는 친구...당신이 할 말은??")
        five = input("ㄱ. 그래. 숙소 가서 쉬장!!   ㄴ. 먼저 숙소 가있어! 나는 좀 보고 갈게   ")

        if five == 'ㄴ':
            score += 1

        if score == 4:
            JP_mbti_result = 'J'

        else:
            JP_mbti_result = 'P'

        print("\nJ와 P 판별 테스트가 종료되었습니다. 수고하셨습니다.")
        break

    else:
        print("다시 입력해 주십시오")