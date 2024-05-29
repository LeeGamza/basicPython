class BigNumberError(Exception): # 사용자 정의 에러
    def __init__(self, msg): # 객체가 생성될 떄 자동으로 호출되는 매직 메소드
        self.msg = msg

    def __str__(self):  # 객체를 문자열로 표현될 때 자동으로 호출되는 매직 메소드
        return "[에러코드 001]" + self.msg


try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError(f"입력 값 : {num1}, {num2}")
    print(f"{num1} / {num2} = {num1 / num2}")
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)