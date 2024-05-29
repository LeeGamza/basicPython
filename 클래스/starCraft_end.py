# 스타크래프트 전반부

# 유닛 생성을 위한 클래스

from random import *

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


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

# 게임 종료
def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1시")

Tank.siege_developed = True
print("[알림] 탱크 시즈모드 업그레이드가 완료되었습니다.")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_siege_mode()
    elif isinstance(unit, Wraith):
        unit.cloaking()

for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5, 20))


game_over()


# 후기

# 인스턴스 객체를 받은 m1, m2, m3, 등이 나중엔 unit.damaged, unit.attack등 다른 클래스들의
# 메소드를 사용하는걸 보아
# 상속을 계속 받아 내려온 Marine, Tank, Wraith의 클래스 호출하나로 Unit, AttackUnit 등의
# 메소드를 사용하는걸 봐 신기했다. 