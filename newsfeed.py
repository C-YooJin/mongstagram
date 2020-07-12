def getPosts(db,user):
    print("")
    print("============= 뉴 스 피 드 =============")
    followings_lst = list(db.users.find({'id':user['id']}, {'_id':0, 'followings':1}))[-1]['followings']
    # followings_post = list(db.post.find({'username':followings}, {'_id':0, 'post':1}))[-1]['post']
    followings = [db.users.find_one({'id':user['id']}, {'_id':0,})]

    for i in range(len(followings_lst)):
        for idx in range(len(followings)):
            if db.post.find_one({'username':followings_lst[i]}) != None:
                print(followings_lst[i], "님의 담벼락 입니다.")
                for num in range(len(list(db.post.find({'username':followings_lst[i]})))):
                    print(list(db.post.find({'username':followings_lst[i]}, {'_id':0, 'post':1}))[num]['post'])
                    print("", end='')
                    print('                 ',list(db.post.find({'username':followings_lst[i]}, {'_id':0, 'date':1}))[num]['date'])
                print("")
                print("=====================================")
            else: print(followings_lst[i], '님의 담벼락에는 포스팅이 없네요.')
    return


"""
It is similar to the function in wall.py
Get posts of your followings.
There can be a few options to sort the posts such as posting date or alphabetical order of following's name.
"""
