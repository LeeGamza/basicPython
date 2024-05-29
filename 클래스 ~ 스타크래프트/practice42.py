# super

# 주석으로 설명을 적긴하였다.
# 하지만 추가적으로 다중상속에 개념에서 super는 다르다
# 다중상속시 super를 사용하면 가장 앞에있는 부모클래스만 접근한다.
# 가령 예를 들어서 Unit,Flyable이 있다면
# super를사용하면 Unit 클래스만 접근을 한다.
# 따라서 다중 상속시에는 하나하나 호출을 해야한다.

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동중 [속도 {self.speed}]")

# 건물 클래스
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        
        # 기존 사용하던 방법
        # Unit.__init__(self, name, hp, 0)
        # self.location = location

        # super(부모클래스의 이름을 적지않고 바로 접근하는 방법)
        super.__init__(name, hp, 0)     # self를 적지않아도 된다.
        self.location = location



# Unit을 상속받은 공격 유닛 생성 클래스

class AttackUnit(Unit):   # Unit 클래스를 상속
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed) # 부모클래스 생성자 호출
        self.damage = damage

    # 공격 메소드
    def attack(self, location):
        print(f"{self.name} : {location}방향으로 적군을 공격합니다. [공격력 : {self.damage}]")

    # 피해당하는 메소드
    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")

        # 체력이 0이하면 파괴 조건
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

# 공중 유닛 속도 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    # 공중 유닛 이동 메소드
    def fly(self, name, location):
        print(f"{name} : {location}방향으로 날아갑니다. [속도 {self.flying_speed}]")

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print(["공중 유닛 이동"])
        self.fly(self.name, location)

supply_depot = BuildingUnit("서플라이 디폿", 500, "5시")

def GameStart():
    print("[알림] 게임을 시작합니다.")
def GameOver():
    pass

GameStart()
GameOver()

            