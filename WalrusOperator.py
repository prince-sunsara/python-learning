""" 
THE WALRUS OPERATOR IN PYTHON
    > The walrus operator is a new addition to python 3.8 and allows you to assign a value to a variable within an expression.
    > this can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.
    :=
"""
# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression



# a = True
# print(a)
# # print(a = False) # error
# print(a := False)


foods = list()

# while True:
#     food = input("What food do you like?\n")
#     if food == "quit":
#         break
#     foods.append(food)
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)
print(foods)