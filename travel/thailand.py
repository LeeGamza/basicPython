class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")


if __name__ == "__main__": # 직접 실행되는 경우
    print("Thailand 모듈을 직접실행")
    print("이 문장은 모듈을 직접 실행할 때만 출력")
else: # 외부에서 호출되어 실행되는 경우
    print("Thailand 모듈을 외부에서 호출")