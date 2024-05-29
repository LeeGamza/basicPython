# 다중 상속

# Unit 생성 클래스

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# Unit을 상속받은 공격 유닛 생성 클래스

class AttackUnit(Unit):   # Unit 클래스를 상속
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 부모클래스 생성자 호출
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
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5) # 이름, 체력, 공격력, 공중 이동속도

valkyrie.fly(valkyrie.name, "3시")