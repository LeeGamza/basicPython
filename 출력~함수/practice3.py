# 애완동물을 소개해 주세요~
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집" + animal + "의 이름은 " + name + "이에요")
print(name + "는 " + str(age) + "살이며," + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))


# 정수와 부울형 값을 문자열과 함께 출력하려면 문자열로 변환해야 합니다.
# str(age)와 str(is_adult)를 사용하여 age와 is_adult를 문자열로 변환하지 않으면
# 문자열과 다른 자료형을 연결하려 할 때 오류가 발생합니다.

# 다른방식도 있습니다.
print(name, "는 ", age, "살이며,", hobby, "을 아주 좋아해요")

# + 대신에 ,를 사용하여서도 가능합니다.
# 단 ,를 사용하면 무조건 한칸이 띄워집니다.
