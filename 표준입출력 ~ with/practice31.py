# 파일 입출력

# score_file = open("score.txt", "w", encoding="utf-8") # w의 의미는 쓰기 이다. 추가해서 저장하면 덮어씌우기 형태이다.
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") # a는 추가이다. 원래 있는 문서에 뒤에 추가내용을 계속 적는 형태이다.
# score_file.write("과학 : 80") # write를 쓰면 줄바꿈이 없다.
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding='utf8')
# print(score_file.read())
# score_file.close()



# 원래 print문에서 end=""은 줄바꿈을 하지않고 진행하지만 readline 메서드의 특성상 \n이 박혀있는 상태로 나온다.
# 만약 end=""을 붙이지 않고 밑에 있는 코드를 친다면 \n이 두번인식하게 되는데
# 그 이유는 print가 줄마다 있기에 print마다 \n + readline 메서드 특성으로 인해 끝에 \n이 적혀 2줄씩 띄워지는것이다

# score_file = open("score.txt", "r", encoding='utf8') # r은 read의 약자로 '읽기'를 말함
# print(score_file.readline(), end="") # readline = 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동 줄바꿈 싫을 시 각 print 줄 끝에 end="" 붙이면됨
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="") 
# score_file.close()

# 몇줄인지 모르는 다른 사람의 파일을 읽을 때
# score_file = open("score.txt", "r", encoding='utf8')
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close


# readline의 반환 타입은 str형식이다
# readlines의 반환 타입은 list형식이다.

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")