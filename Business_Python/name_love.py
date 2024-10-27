# 이름궁합 프로그램

from jamo import h2j, j2hcj

print('♡이름 궁합 프로그램♡\n')
name1 = input('당신의 이름은? ')
name2 = input('상대의 이름은? ')

new_1 = []
new_2 = []

z = {'ㅂ':4, 'ㅃ':8, 'ㅍ':4, 'ㅁ':4, 'ㄷ':3, 'ㄸ':6, 'ㅌ':4, 'ㅅ':2, 'ㅆ':4, 'ㄴ':2,
     'ㄹ':5, 'ㅈ':3, 'ㅉ':6, 'ㅊ':4, 'ㄱ':2, 'ㄲ':4, 'ㅋ':3, 'ㅇ':1, 'ㅎ':3}
m = {'ㅏ':2, 'ㅑ':3, 'ㅓ':2, 'ㅕ':3, 'ㅗ':2, 'ㅛ':3, 'ㅜ':2, 'ㅠ':3, 'ㅡ':1, 'ㅣ':1,
     'ㅐ':3, 'ㅒ':4, 'ㅔ':3, 'ㅖ':4, 'ㅘ':4, 'ㅙ':5, 'ㅝ':4, 'ㅞ':5, 'ㅢ':2, 'ㅚ':3,
     'ㅟ':3}

# 분리한 글자수 세기

for i in range(len(name1)):
     name_list_1 = list(j2hcj(h2j(name1[i])))
     for j in range(len(name_list_1)):
          if name_list_1[j] in z:
               name_list_1[j] = z[name_list_1[j]]
          else:
               name_list_1[j] = m[name_list_1[j]]
     new_1.append(sum(name_list_1))

for i in range(len(name2)):
     name_list_2 = list(j2hcj(h2j(name2[i])))
     for j in range(len(name_list_2)):
          if name_list_2[j] in z:
               name_list_2[j] = z[name_list_2[j]]
          else:
               name_list_2[j] = m[name_list_2[j]]
     new_2.append(sum(name_list_2))

repeat = []

for i in range(len(new_1)):
     repeat.append((new_1[i] + new_2[i]) % 10)

repeat_1 = []

repeat_1.append(repeat[0] + repeat[1])
repeat_1.append(repeat[2])

if repeat_1[0] >= 10:
     repeat_1[0] = repeat_1[0] % 10
if repeat_1[1] >= 10:
     repeat_1[1] = repeat_1[1] % 10

final = int(f'{repeat_1[0]}' + f'{repeat_1[1]}')

print('\n♡결과♡')
print(f'{name1}과 {name2}의 궁합은 {final}% 입니다♡')

if final >= 90:
     print(f'{name1}과 {name2}는 운명의 상대♡')
elif final >= 70 and final < 90:
     print(f'{name1}과 {name2}는 베프♡')
elif final >= 50 and final < 70:
     print(f'{name1}과 {name2}는 칭긔칭긔')
elif final >= 30 and final < 50:
     print(f'{name1}과 {name2}는 안맞아..ㅠㅠ')
else:
     print(f'{name1}과 {name2}는 전생의 웬수??!')