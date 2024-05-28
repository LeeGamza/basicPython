# Quiz) 표준 체중을 구하는 프로그램을 작성하시오
# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) * 키(m) * 22
# 여자 : 키(m) * 키(m) * 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#             * 함수명 : std_weight
#             * 전달값 : 키(height), 성별(gender)
# 조건2 :     표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

from math import *

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    elif gender == "여자":
        return height * height * 21
    else:
        print("잘못된 성별입니다.")    

height, gender = input("키(cm)와 몸무게를 입력하십시오 : ").split()

height = float(height) / 100
weight = std_weight(height, gender)
print(f"키 {int(height * 100)}cm {gender}의 표준 체중은 {weight:.2f}kg 입니다.")