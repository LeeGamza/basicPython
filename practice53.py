# 내장 함수

# input과 print 내장함수

# language = input("무슨 언어를 좋아하세요?")
# print(f"{language}은 아주 좋은 언어입니다!")

# dir 내장함수
# dir()은 어떤 객체를 넘겼을 떄 그 객체가 어떤 변수와 함수를 가지고 있는지
# 알려주는 목적으로 사용할 수 있다.

# 만약 전달 값으로 아무것도 넘기지 않는다면 현재 소스코드 범위 내에서
# 사용 가능한 모듈 또는 객체가 출력된다.

print("아무것도 import하지 않았을떄\n-----------------------")
print(dir())
import random
print("추가로 random을 import했을 때\n-----------------------")
print(dir())
import pickle
print("추가로 pickle을 import했을 때\n-----------------------\n")
print(dir())
print("랜덤 모듈만 dir()을 했을 때\n-----------------------")
print(dir(random))

print("리스트 자료구조룰 하나 만들어 리스트에서 사용 가능한 변수\n함수 목록들을 보여줌\n\
      -----------------------\n\n")
lst = [1,2,3]
print(dir(lst))

print("문자열 변수를 만들어 문자열에서 사용가능한 변수와\n함수 목록들을 보여줌\n\
      -----------------------\n\n")

name = "Jin"
print(dir(name))

# 그외 내장함수들은 여기를 참조
# 링크 : https://docs.python.org/3/library/functions.html )
