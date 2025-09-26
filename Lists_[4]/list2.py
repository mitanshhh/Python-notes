fruits = ["Apple", "Banana", "Melon"]

#APPEND METHOD
#Inserts at the last of the list 
fruits.append("Strawberry")
print(fruits)


#INSERT METHOD
#Inserts at the given index
fruits.insert(0, "Kiwi") #index is 0 so it will appear first
print(fruits)


#REMOVE METHOD
#Removes the word
fruits.remove("Apple")
print(fruits)

#CHANGING CONTENT
fruits[2] = "Grapes"
print(fruits)