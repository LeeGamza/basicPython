# 클래스

# 클래스를 쓰지않을 시 유닛하나마다 변수를 적어서 생성해야함

# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음

# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print(f"{name} 유닛이 생성되었습니다.")
# print(f"체력 : {hp}, 공격력 : {damage}\n")

# # 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반 모드 / 시즈 모드

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print(f"{tank_name} 유닛이 생성되었습니다.")
# print(f"체력 : {tank_hp}, 공격력 : {tank_damage}")

# def attack(name, location, damage):
#     print(f"{name} : {location} 방향으로 적군을 공격 합니다. [공격력 {damage}]")

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성 되었습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}")

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
