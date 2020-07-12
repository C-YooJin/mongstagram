def search(db, user):
    print("")
    print("============포 스 트 검 색=============")
    key_word = input("검색할 해시태그를 # 없이 입력해주세요: ")
    print("")
    print("====================================")
    hash_post = db.post.find({'hashtag': key_word})
    for i in hash_post:
        print(i['post'])
        print('          ', i['username'], '/', end=" ")
        print(i['date'])
    print("====================================")
    print("")
    print('(1) 다른 키워드로 검색')
    print('(2) 이전 페이지로')
    print('(3) 프로그램 종료 ')
    num = input('원하는 기능을 선택하세요: ')

    if int(num) == 1:
        search(db, user)
    elif int(num) == 2:
        return
    elif int(num) == 3:
        print('프로그램이 종료됩니다.')
        exit()
    else:
        print("에잉, 아무거나 눌렀기 때문에 너도 종료.")
        exit()