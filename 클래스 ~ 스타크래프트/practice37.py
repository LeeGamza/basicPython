# method(메소드)

# 일반 함수와 다른점
# 메소드는 전달 값을 정의하는 부분 처음에 self를 적어준다는 점
# 메소드 내에서 self.을 통해 클래스 멤버변수에 접근 가능하다는 점

class AttackUnit:   # 공격유닛 클래스
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
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

# 추가로 햇갈려서 정리한 내용
# 인스턴스 변수: self를 통해 접근.
# 클래스 변수: ClassName.variable을 통해 접근 (명확성과 일관성을 위해).

