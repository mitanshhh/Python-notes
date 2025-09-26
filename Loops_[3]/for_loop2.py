
number = int(input("Display multiplication table of? "))
max_limit = number*10+1
y = 1


for answer in range(number, max_limit, number):
    print( str(number) + " x " + str(y) + " = " + str(answer))
    y += 1