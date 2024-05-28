# 가변 인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")  # end = " " = 줄바꿈하지않고 바로 이어서 출력
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")  # end = " " = 줄바꿈하지않고 바로 이어서 출력
    for lang in language:
        print(lang, end = " ")
    print()


profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")
