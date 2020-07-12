from user import *
import datetime
import re

def postInterface(db, user):
    post = list(db.post.find({"username": user['id']},
                             {'_id': 0,
                              'username': 1, 'pid':1, 'post':1, 'date':1}))
    print("")
    print("============= 담  벼  락 =============")

    for idx in range(len(post)):
        print(post[idx]['pid'], "-", end=" ")
        print(post[idx]['post'])
        print('          ', post[idx]['username'], '/', end=" ")
        print(post[idx]['date'])

    print("=====================================")
    # for key, value in range((db.post.find().count()) -1):
    #    print(post[value], end=" ")
    print("")
    print("(1) 이전 페이지로")
    print("(2) 포스트 삭제하기 ")
    print("(아무 숫자나 입력) 프로그램 종료 ")
    print("")
    num = input("원하는 기능을 선택하세요: ")
    if int(num) == 1:
        return
    elif int(num) == 2:
        deletePost(db, user)
    else:
        exit()
    """
    Implementing the interface to post your text.
    There are three or more items to choose functions such as inserting and deleting a text.
    """

def insertPost(db, user):
    print("")
    print("===========포 스 팅 페 이 지============")
    print("담벼락에 포스팅 할 내용을 입력하세요.")
    print("해시태그는 포스트 작성을 완료 한 후에 따로 작성 가능합니다.")
    post = input('POST => ')
    now = datetime.datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')

    if len([db.users.find_one({'id':user['id']}, {'_id':0, 'pid_lst':1})][-1]['pid_lst']) == 0:
        pid = 1
        db.users.update({'id':user['id']}, {'$push': {'pid_lst':pid}})
        db.post.insert_one({'username': user['id'], 'pid': pid, 'post': post, 'date': date})
    else:
        pid = max([db.users.find_one({'id':user['id']}, {'_id':0, 'pid_lst':1})][-1]['pid_lst']) + 1
        db.users.update({'id':user['id']}, {'$push': {'pid_lst':pid}})
        db.post.insert_one({'username': user['id'], 'pid': pid, 'post': post, 'date': date})

    print(" ")
    tag = input("해시태그를 입력하시겠습니까? (y/n): ")
    if tag == 'y':
        content = input("해시태그를 입력해주세요(ex. #SNS #mongsta): ")
        content = content.split(" ")
        for i in content:
            new = i.lstrip('#')
            db.post.update({'username':user['id']}, {'$push':{'hashtag':new}})
    else:
        print('포스팅 완료')

    postInterface(db, user)

    '''
    Insert user's text. You should create the post schema including,
    for example, posting date, posting id or name, and comments.
    You should consider how to delete the text.
    '''

def deletePost(db, user):
    number = eval(input("삭제할 포스팅 번호를 입력하세요: "))
    check = input("정말 지우시겠습니까?(y/n): ")
    if check == 'y':
        db.post.remove({'pid': number})
        db.users.update({'id':user['id']}, {'$pull': {'pid_lst': number}})
        postInterface(db, user)
    else:
        print("")
        print("이전 페이지로 돌아갑니다.")
        postInterface(db, user)
    """
    Delete user's text.
    With the post schema, you can remove posts by some conditions that you specify.
    """

    """
    Sometimes, users make a mistake to insert or delete their text.
    We recommend that you write the double-checking code to avoid the mistakes.
    """
