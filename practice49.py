# __all__

# import * 은 모든 것을 가져다 쓰겠다는 의미
# 그렇지만 사실은 패키지를 만든 사람이 공개범위를 설정해줄 수 있는것

# 현재 travel 디렉토리안에 __init__에 베트남 모듈만 공개설정

# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


# 하지만 태국은 공개하지 않았기에 나오지 않음

# from travel import * 
# trip_to = thailand.ThailandPacakge()
# trip_to.detail()



# travel 디렉토리 안에 __init__에 태국 모듈도 공개 설정


from travel import * 
trip_to = thailand.ThailandPackage()
trip_to.detail()
