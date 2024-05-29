# 예외처리

# try:
#     print("나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요: "))
#     num2 = int(input("첫 번째 숫자를 입력하세요: "))
#     print(f"{num1} / {num2} = {num1 / num2}")
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요: ")))
    nums.append(int(input("두 번째 숫자를 입력하세요: ")))
    nums.append(int(nums[0] / nums[1]))
    print(f"{nums[0]} / {nums[1]} = {nums[2]}")
except ValueError: # 잘못된 타입 넣을 시 예외처리
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # 0으로 나누려고 할 때 예외처리
    print(err)
except Exception as err: # 나머지 에러들 예외처리
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)