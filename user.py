from post import *
from follow import *
from newsfeed import *
from search import *
import time


def signup(db):
    '''
    1. Get his/her information.
    2. Check if his/her password equals confirm password.
    3. Check if the userid already exists.
    4. Make the user document.
    5. Insert the document into users collection.
    '''
    print("============ 회 원 가 입 ==============")
    id = input('가입할 아이디 입력: ')
    if db.users.find({'id':id}).count() == 0:
        check = False
    else: check = True

    while check:
        id = input("아이디가 이미 있습니다. 다시 입력하세요:  ")
        if db.users.find({"id":id}).count() == 0: break
        else: check = True

    # Check if his/her password equals confirm password.
    password = input("가입할 비밀번호 입력: ")
    c_password = input("똑같이 한 번 더 입력: ")
    if password != c_password: confirm_password = True
    else: confirm_password = False

    while confirm_password:
        c_password = input("비밀번호가 서로 달라요 다시 입력하세요: ")
        if password == c_password: break
        else: confirm_password = True

    sex = input("성별 입력(F or M): ")
    age = input("나이: ")
    db.users.insert({"id":id, "password":password, "sex":sex, "age":age,
                     "followers": [], 'followings': [], 'pid_lst': []})
    print("회원가입 성공^0^")
    signin(db)
    return

def signin(db):
    '''
    1. Get his/her information.
    2. Find him/her in users collection.
    3. If exists, print welcome message and call userpage()
    '''
    print("")
    print("============== 로 그 인 ==============")
    id = input("아이디:")
    password = input("비밀번호: ")
    print("=====================================")
    if db.users.find({"id":id, "password":password}).count() == 1: check = False
    else: check = True
    

    while check:
        print("아이디나 비밀번호가 틀렸습니다.")
        id = input("아이디를 다시 입력하세요:  ")
        password = input("비밀번호도 다시 입력하세요: ")
        if db.users.find({"id":id, "password":password}).count() == 1: break
        else: check = True
    print("")
    print("============== 로그인 성공 =============")
    time.sleep(0.3)
    print("")
    print("========== 곧 시작됩니다 ๑•‿•๑ =========")
    user = db.users.find_one({'id': id})
    # user_id = list(db.users.find({'id': id, 'password': password}))[0]
    # _init_status(db, user_id)
    time.sleep(1)
    print("")
    print(" Mongstagram에 오신 것을 환영합니다!")
    userpage(db, user)

def mystatus(db, user):
    print("")
    print(user['id'], "회원님의 상태를 보여주는 페이지 입니다.")
    print(user['id'],'님의 성별은', user['sex'], '이며, 나이는 한국나이로', user['age'],'세 입니다.')
    print('Followers:', len([db.users.find_one({'id':user['id']}, {'_id':0, 'followers':1})][-1]['followers']),
          '/ Followings:', len([db.users.find_one({'id':user['id']}, {'_id':0, 'followings':1})][-1]['followings']))
    print("")
    print('이전 페이지로 돌아가시겠습니까?')
    back = input('(y:돌아가기 / n:프로그램 종료): ')
    if back == 'y':
        userpage(db, user)
    elif back == 'n':
        return exit()
    else:
        print(".....")
        time.sleep(1)
        print("아무거나 눌렀으니까 너도 저리가 에잉")
        time.sleep(1)
        return exit()
    '''
    print user profile, # followers, and # followings
    '''

def userpage(db, user):
     while True:
        print("")
        time.sleep(0.5)
        print("(1) 내 상태창")
        print('(2) 뉴스피드 ')
        print('(3) 담벼락 ')
        print('(4) 포스팅 하기 ')
        print('(5) 팔로우 하기 ')
        print('(6) 팔로우 끊기 ')
        print('(7) 포스트 검색 ')
        print('(8) 로그아웃')
        print("")
        num = input("원하는 기능을 선택하세요: ")
        if int(num) == 1:
            mystatus(db, user)
        elif int(num) == 2:
            getPosts(db, user)
        elif int(num) == 3:
            postInterface(db, user)
        elif int(num) == 4:
            insertPost(db, user)
        elif int(num) == 5:
            follow(db, user)
        elif int(num) == 6:
            unfollow(db, user)
        elif int(num) == 7:
            search(db, user)
        elif int(num) == 8:
            return exit()
        else: return
        '''
        user page
        '''
