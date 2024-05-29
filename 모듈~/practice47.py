# 모듈

# import theater_module

# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_solider(5)



# 모듈이름이 너무길면, 별명을 붙일 수 있다.
# import theater_module as movie

# movie.price(3)
# movie.price_morning(4)
# movie.price_solider(5)



# from ~ import 구문을 써보자
# from theater_module import *

# 귀찮게 모듈명.함수이름을 적을 필요가 없어졌다.
# 그냥 모듈 내 함수이름만 적어도 실행이된다

# price(3)
# price_morning(4)
# price_solider(5)



# 이번엔 일반가격과 조조할인 가격만 들고와보자
# from theater_module import price, price_morning

# price(5)
# price_morning(6)
# price_solider(7) # 사용불가


# 이번엔 from ~ import 구문에도 별명을 붙여보자

from theater_module import price_solider as price
price(5)