# pass

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
        pass # 정의하지 않고 일단 건너간다.

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

            