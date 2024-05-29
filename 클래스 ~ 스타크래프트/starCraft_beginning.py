# 스타크래프트 전반부

# 유닛 생성을 위한 클래스

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{self.name}이 생성되었습니다.")
    
    def move(self, location):
        print(f"{self.name} : {location} 방향으로 이동중 [속도 {self.speed}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")

        # 체력이 0이하면 파괴 조건
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")


class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed) 
        self.damage = damage


    def attack(self, location):
        print(f"{self.name} : {location}방향으로 적군을 공격합니다. [공격력 : {self.damage}]")

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed


    def fly(self, name, location):
        print(f"{name} : {location}방향으로 날아갑니다. [속도 {self.flying_speed}]")

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)


# 유닛 클래스
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 5, 1)

    def stimpack(self):
        if self.hp > 10:
            print(f"{self.name}이 스팀팩을 사용하였습니다.")
            self.hp -= 10
        else:
            print(f"{self.name}의 체력이 낮아 스팀팩을 사용하지 못했습니다.")

class Tank(AttackUnit):
    siege_developed = False
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 35, 1)
        self.siege_mode = False

    def set_siege_mode (self):
        if Tank.siege_developed == False:
            return
        
        if self.siege_mode == False:
            print(f"{self.name} : 시즈모드로 전환합니다.")
            self.damage *= 2
            self.siege_mode = True
            self.speed = 0
            
        else:
            print(f"{self.name} : 시즈모드를 해제합니다.")
            self.damage /= 2
            self.siege_mode = False
            self.speed = 1

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.cloaking == False

    def cloaking(self):
        if self.cloaking == True:
            print(f"{self.name} : 클로킹 상태를 해제합니다.")
            self.cloaking = False
        else:
            print(f"{self.name} : 클로킹 모드로 전환합니다.")
            self.cloaking = True
