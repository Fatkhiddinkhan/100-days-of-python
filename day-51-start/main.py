from SpeedCheck import InternetSpeedTwitterBot

DOWN = 500
UP = 100

user_prompt = input("Enter your Twitter username: ")
password_prompt = input("Enter you Twitter password: ")

twit_bot = InternetSpeedTwitterBot(user_prompt, password_prompt)
twit_bot.get_internet_speed()
twit_bot.tweet_at_provider()
