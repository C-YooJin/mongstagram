# main.py
from user import *
from pymongo import MongoClient

client = MongoClient()
db = client.mong     # db 이름 설정해주는 부분

def mainpage(db):
    print("")
    print("*==========S2 Mongstagram S2==========*")
    print("|    1. 회원가입       ()()            |")
    print("|    2. 로그인        ( . .)   ㅡ Hi   |")
    print("|    0. sns 종료     (     )           |")
    print("*=====================================*")
    print("")
    number = eval(input("0, 1, 2중 원하는 숫자를 입력하세요: "))
    if number in [0, 1, 2]:
        if number == 0:
            exit(); return
        elif number == 1:
            signup(db)
        elif number == 2:
            signin(db)
    else: print("0, 1, 2중 입력하라니까.. 프로그램을 다시 시작하세요.")
    '''
    call signup() or signin()
    '''
def exit():
    print("잘가랏")
    return

if __name__ == "__main__":
    mainpage(db)
    '''
    call mainpage()
    '''
