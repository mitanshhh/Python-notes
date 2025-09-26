username = input("Write your username: ")

def chk_uname(username):
    if len(username) > 3:
        print("This username is valid")
    elif len(username) < 3:
            print( "This username is too short")

def uname():
    chk_uname(username)
    print("Your username is " + username)

uname()
