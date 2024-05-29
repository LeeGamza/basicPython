# init과 instance
# init은 타언어에서의 생성자이다.

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성 되었습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}")

marine1 = Unit("마린", 40, 5) # instance
marine2 = Unit("마린", 40, 5) # instance
tank = Unit("탱크", 150, 35) # instance
