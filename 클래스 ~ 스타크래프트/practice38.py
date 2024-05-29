# 상속

# 재사용성과 확장성을 높이기 위해 사용
# 1. 코드 재사용 : 기존 클래스의 기능을 재사용하여 새로운 클래스를 만들 수 있다.
#                 코드 중복을 줄이고, 유지보수가 쉬워진다.

# 2. 확장성 : 기존 클래스를 확장하여 새로운 기능을 추가할 수 있다.
#            기존 코드를 수정하지 않고 새로운 기능을 구현 할 수 있다.

# 3. 계층 구조 : 클래스 간의 계층 구조를 만들어 더 논리적이고 관리하기 쉬운 코드를 작성할 수 있다.

# 4. 부모 클래스 타입의 변수가 자식 클래스 객체를 참조할 수 있어 다양한 객체를 다룰 수 있다.

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit):   # Unit 클래스를 상속
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 부모클래스 생성자 호출
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location}방향으로 적군을 공격합니다. [공격력 : {self.damage}]")


    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")

        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)