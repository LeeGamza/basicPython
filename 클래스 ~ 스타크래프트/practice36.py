# 멤버 변수
# 멤버 변수에는 클래스 변수와 인스턴스 변수가 있다.
# 인스턴스 변수는 생성자 안에 위치해 있으며, 객체가 생성될 때마다 새로 만들어진다.
# 클래스 변수는 클래스 안에 있으며, 생성자 안에 위치하지 않는다.
# 인스턴스 변수는 각 객체마다 독립적으로 존재한다.
# 클래스 변수는 클래스 내의 모든 객체에 의해 공유된다.

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name # 인스턴스 변수
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성 되었습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}")

# marine1 = Unit("마린", 40, 5) # instance
# marine2 = Unit("마린", 40, 5) # instance
# tank = Unit("탱크", 150, 35) # instance

# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}")

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (뺴앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.cloaking = True # 외부에서 생성된 인스턴스 변수로 다이나믹 인스턴스 변수 또는 동적 속성이라 한다.

if wraith2.cloaking == True: 
    print(f"{wraith2.name}는 현재 클로킹 상태입니다.")