# 함수 전달값과 반환값

def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if money > balance:
        print("잔액이 부족합니다.")
        return balance
    else :
        print(f"{money}원이 출력되었습니다. 남은 잔액은 {balance - money}원 입니다.")
        return balance - money

balance = 1000 # 잔액
# # balance = deposit(balance, 1000)
# # print(balance)
# balance = deposit(balance, 1000)
# print(balance)

# balance = withdraw(balance, 500)
# print(balance)

def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

commission, balace = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balace))