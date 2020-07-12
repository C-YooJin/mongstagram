def follow(db, user):
    print("")
    print("============ 팔로우 페이지 =============")
    following_id = input("팔로우 하고자 하는 ID를 입력하세요: ")
    if user['id'] != following_id:
        if db.users.find_one({'id':following_id}):
            # 회원 목록에 아이디가 존재하기 때문에 팔로우 가능
            if db.users.find_one({'id':following_id, 'followers':user['id']}, {'_id':0, 'followers':1}) == None:
                # 상대방의 팔로우 목록에 내가 존재하지 않을 경우 팔로잉 한다.
                db.users.update({'id':user['id']}, {'$push': {'followings':following_id}})
                db.users.update({'id':following_id}, {'$push': {'followers':user['id']}})
                print("")
                print("\"", following_id, "\"", '님의 followers 목록에 회원님이 추가되었습니다.')
                print("회원님의 followings 목록에", "\"", following_id, "\"", '님이 추가되었습니다.')
            else:
                print("")
                print("상대방의 팔로우 목록에 회원님이 이미 존재합니다.")
                print("이전 페이지로 돌아갑니다.")
                return
        else:
            print("")
            print("존재하지 않는 사용자입니다.")
            print("이전 페이지로 돌아갑니다.")
            return
    else:
        print("스스로는 팔로우 할 수 없습니다.")

    '''
        1. 팔로우하고자 하는 유저가 존재하는지 확인, 없으면 경고 출력

        2. 팔로우하고자 하는 유저가 나의 팔로잉 목록에 있는지 확인, 있으면 경고 출력

        3. 팔로잉 목록에 없으면,
            나의 팔로잉 목록에 팔로우할 유저id 추가 + 상대방의 팔로워 목록에 내 id 추가
    '''
def unfollow(db, user):
    print("")
    print("============= 팔로우 끊기 =============")
    unfollow_id = input("팔로우 끊을 ID를 입력하세요: ")
    if db.users.find_one({'id':unfollow_id}):
        # 회원 목록에 아이디가 존재하기 때문에 언팔로우 가능
        if db.users.find_one({'id':unfollow_id, 'followers':user['id']}, {'_id':0, 'followers':1}):
            # 상대방의 팔로우 목록에 내가 존재하기 때문에 언팔로우 가능
            db.users.update({'id':unfollow_id}, {'$pull': {'followers':user['id']}})
            db.users.update({'id':user['id']}, {'$pull': {'followings':unfollow_id}})
            print("")
            print("\"", unfollow_id, "\"", '님의 followers 목록에 회원님이 삭제되었습니다.')
            print("회원님의 followings 목록에", "\"", unfollow_id, "\"", '님이 삭제되었습니다.')
        else:
            print("")
            print("상대방의 팔로우 목록에 회원님이 존재하지 않습니다.")
            print("이전 페이지로 돌아갑니다.")
            return
    else:
        print("")
        print("존재하지 않는 사용자입니다. ")
        print("이전 페이지로 돌아갑니다.")
        return

    """
        1. 언팔로우하고자하는 유저가 존재하는지 확인, 없으면 경고 출력

        2. 언팔로우하고자 하는 유저가 나의 팔로잉 목록에 있는지 확인, 없으면 경고 출력

        3. 팔로잉 목록에 있으면,
            나의 팔로잉 목록에서 언팔로우할 유저id 제거 + 상대방의 팔로워 목록에서 내 id 제거
    """