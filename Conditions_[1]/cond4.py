#We can make very complex comparisons by joining statements together using logical operators with our comparison operators. These logical operators are and, or, and not. When using the and operator, both sides of the statement being evaluated must be true for the whole statement to be true. When using the or operator, if either side of the comparison is true, then the whole statement is true. Lastly, the not operator simply inverts the value of the statement immediately following it. So if a statement evaluates to True, and we put the not operator in front of it, it would become False.

#For "and" both statements should be true
print("dog" == "cat" and "cat" == "cat")

print("dog" == "dog" and "cat" == "cat")

#For "or" one statements should be true

print("dog" == "cat" or 1 != 1)

print("dog" == "cat" or 1 != 2)

#Converts true into false and false into true

print(not 1 == 1) 

print(not "cat" == 1)
