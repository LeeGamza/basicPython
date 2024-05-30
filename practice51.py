import inspect
# from travel_temp import thailand
# travel 폴더를 random 폴더로 옮기기 전

from travel import thailand
import random
print(inspect.getfile(random))

# c:\Users\hoon3\AppData\Local\Programs\Python\Python312\Lib\random.py

# print(inspect.getfile(thailand))

# C:\basicPython\travel\thailand.py

# 이후 random 모듈이 있는 폴더로 travel 폴더를 옮김

print(inspect.getfile(thailand))

# c:\Users\hoon3\AppData\Local\Programs\Python\Python312\Lib\travel\thailand.py

# 이후 모든 파일은 제자리로 돌림