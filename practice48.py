# 패키지

# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()



# 단 import 구문에서 클래스나 함수는 import 불가

# ex) import travel.thailand.ThailandPackage 
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()


# from ~ import 구문은 가능

from travel.thailand import ThailandPackage
from travel import vietnam

trip_to = ThailandPackage()
trip_to.detail()

trip_to2 = vietnam.VietnamPackage()
trip_to2.detail()