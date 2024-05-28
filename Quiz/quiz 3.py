# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
# --당첨자 발표--
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다. --

# (활용 예제)

from random import *
# 방법 1

# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(lst)
# print(f'''--당첨자 발표--
# # 치킨 당첨자 : {sample(lst, 1)}
# # 커피 당첨자 : {sample(lst, 3)}
# # -- 축하합니다. --''')

# 방법 2

# lucky = []
# for i in range(1,21,1):
#     lucky.append(i)
# shuffle(lucky)
# print(f'''--당첨자 발표--
# # 치킨 당첨자 : {sample(lucky, 1)}
# # 커피 당첨자 : {sample(lucky, 3)}
# # -- 축하합니다. --''')

# 방법 3
users = list(range(1, 21)) # 1부터 20까지 숫자를 생성.
shuffle(users)
print(f'''--당첨자 발표--
치킨 당첨자 : {sample(users, 1)}
커피 당첨자 : {sample(users, 3)}
-- 축하합니다. --''')

# 오늘안 사실
# range로 만든 users1의 객체를 하나씩 인덱싱 하면
# 놀랍게도 그 타입은 int형임

users1 = range(1,21) # 1부터 20까지 생성
print(users1) # range(1,21)
print(users1[0]) # 1
print(users1[1]) # 2 타입 먼지암? int임
print(type(users1[1]))

# range는 int형만 받음 float나 다른 형식은 받지 않음
# 따라서 range로 만들어진 숫자들은 type이 int형 인거임