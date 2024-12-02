class User:
    def __init__(self, user_id, username, ):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.followings = 0

    def follow(self, user):
        user.followers += 1
        self.followings += 1
user_1 = User('12', 'mike',)
user_2 = User('23', 'nancy')

user_2.follow(user_1)
print(user_2.followers)

