from InstaBot import InstaFollowersBot

username = input("Enter your username: ")
password = input("Enter your password: ")
target_user = input("Enter nickname: ")


bot = InstaFollowersBot(username=username, password=password,target_account=target_user)
bot.insta_login()
bot.fetch_full_info()

