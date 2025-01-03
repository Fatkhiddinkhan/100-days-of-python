class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(*args, **kwargs)
        if args[1] < 18:
            print("You are and adult")

    return wrapper

@is_authenticated_decorator
def create_blog_post(user, age):
    print(f"This is {user}'s new blog post.User {age} years old")

new_user = User('Mike', 20)
new_user.is_logged_in = True
create_blog_post(new_user.name, new_user.age)