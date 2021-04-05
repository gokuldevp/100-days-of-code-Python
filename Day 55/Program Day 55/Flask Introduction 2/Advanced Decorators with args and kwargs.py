class User:
    def __init__(self, name):
        self.username = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
        else:
            print("Login first")
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is a blog post by {user.username}.")


new_user = User("Gokul")

create_blog_post(new_user)

new_user.is_logged_in = True

create_blog_post(new_user)

