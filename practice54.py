# 외장 함수

# 먼저 Google에 list of python modules 를 검색

# 이번 예제에서는 glob을 써보자
# glob은 어떤 경로 내의 폴더 또는 파일의 목록을 조회 할때 사용

# import glob
# print(glob.glob("*.py"))

# os 모듈을 사용하여 보자
# os 운영체제에서 제공하는 기본 기능을 쓸 수있다.

# import os
# print(os.getcwd()) # 현재 디렉토리를 나타냄



# 폴더 생성을 해보자

# folder = "sample_dir"

# if os.path.exists(folder): # 폴더가 존재한다면
#     print("이미 존재하는 폴더입니다.")
# else: # 폴더가 존재하지 않으면
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")



# 이제 해당 폴더가 존재하면 삭제를 해보자

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder) # 폴더 삭제
#     print(folder, "폴더를 삭제하였습니다.") # 삭제 문구 출력
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")




# os에서 제공하는 모듈에 listdir()이라는 것이 있는데
# glob 모듈의 glob()함수와 비슷하게 현재 작업 디렉토리 내의 폴더와 파일 목록을 출력해줌

# import os
# print(os.listdir())


# 시간관련 함수를 제공하는 time 모듈

# import time
# print(time.localtime())

# print("\n한국식과 비교하기 위한 구분선 -------------------\n")

# # 한국 날짜 정보처럼 편집해보자 년/월/일

# print(time.strftime("%Y년%m월%d일 %H시%M분%S초"))



# time과 비슷한 모듈로 datetime도 있다.

import datetime
print("오늘 날짜는", datetime.date.today())

# timedelta() 라는 함수는 두 날짜 사이의 간격을 쉽게 계산할 수 있다.
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은", today+td)