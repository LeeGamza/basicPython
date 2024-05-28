# continue / break

absent = [2, 5] # 결석
no_book = [7] # 책을 깜박했음
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print(f"오늘 수업 여기까지. {student}는 교무실로 따라와")
        break
    print(f"{student}, 책을 읽어봐")
    