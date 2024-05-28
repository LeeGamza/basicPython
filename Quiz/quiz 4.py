# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# ...
# [] 50번째 손님 (소요시간 :16분)

# 총 탑승 승객 : 2 분

from random import *

count = 0
for customer in range(1,51):
    timer = randint(5, 50)
    if 5 <= timer <= 15:
        count+= 1
        print(f"[O] {customer}번째 손님 (소요시간 : {timer})")
    else:
        print(f"[ ] {customer}번째 손님 (소요시간 : {timer})")
        
print(f"총 탑승 승객 : {count} 분")



# 오답 주의하자!!!
# 내가 작성한 코드

# from random import *

# timer = randint(5, 50)
# count = 0
# for customer in range(1,51):
#     print(f"{customer}번째 손님 (소요시간 : {timer})")
#     if 5 <= timer <= 15:
#         count+= 1

# print(f"총 탑승 승객 : {count} 분")


# 잘못된건 for문 밖에 난수 생성기를 넣음으로 인해
# timer가 딱 한번 난수를 생성하고 고정이 되어버림
# 따라서 for문안에 timer 난수를 적으면
# 계속 timer변수는 난수를 새로 받아서 값을 넣게됨!!