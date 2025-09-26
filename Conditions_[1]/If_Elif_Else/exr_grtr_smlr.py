def is_what(number):
    if number > 0:
        print("The number " + str(number) + " is greater than zero")
    elif number < 0:
        print("The number " + str(number) + " is smaller than zero")
    else:
         print("Invalid user input")

is_what(5)
is_what(-1)
