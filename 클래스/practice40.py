# 메소드 오버라이딩

# 일반 유닛 생성 클래스

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동중 [속도 {self.speed}]")

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

vulture1 = AttackUnit("벌쳐", 100, 6, 10)
battleCruze = FlyableAttackUnit("배틀크루저", 500, 20, 3)

vulture1.move("5시")
battleCruze.move("5시")
            
            