def check_user(func):
    def wrapper(user):
        if user != "admin":
            print("Access denied")

        else:
            func(user)
            return
    return wrapper

@check_user
def view_dash_board(user):
    print(f"Welcome {user} here is dashboard")

# function is calling
# view_dash_board("guest")
view_dash_board("admin")
