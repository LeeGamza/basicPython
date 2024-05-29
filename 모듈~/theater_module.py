# theater_module
# 모듈

# 이 파일은 모듈이 되며 다른 파일에서 가져다가 사용할 수 있습니다. 여러분이 원래 사용하시던 파일 (ex : practice.py) 에서 모듈을 사용해볼텐데,
# 주의할 점은 theater_module.py 파일과 이 모듈을 사용할 파일은 서로 같은 경로상에 있어야 한다는 것입니다.

def price(people):
    print(f"{people}명 가격은 {people * 10000}원 입니다.")

def price_morning(people):
    print(f"{people}명 조조 할인 가격은 {people * 6000}원 입니다.")


def price_solider(people):
    print(f"{people}명 군인 할인 가격은 {people * 4000}원 입니다.")