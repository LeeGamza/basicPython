# 문자열 처리 함수

python = "Python is Amazing"
print(python.lower()) # 소문자로 출력
print(python.upper()) # 대문자로 출력
print(python[0].isupper()) # 0번째 글짜가 대문자입니까?
print(len(python)) # 파이썬변수의 길이
print(python.replace("Python", "Java")) # 글자 바꾸기

index = python.index("n") # 제일 처음에 발견하는 'n'이라는 글자의 위치
print(index)
index = python.index("n", index + 1) # 제일 처음에 발견하는 n말고 그 이후에 나오는 n의 위치
print(index)

print(python.find("n")) # 제일 처음에 발견하는 n의 위치
print(python.find("Java")) # 변수에 찾는 문자가 없다면 -1을 반환

# print(python.index("Java")) # index에는 찾는 문자가 없다면 오류발생

print(python.count("n")) # 변수에 찾는 문자열의 개수