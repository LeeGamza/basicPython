# 튜플 (변경되지않는 목록을 사용할때 씀 {속도는 리스트보다 빠름})

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") # 튜플은 add라는 함수를 제공하지않는다.

# name = "김종국"
# age = 20
# hobby = "운동"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "운동")
print(name,age,hobby)