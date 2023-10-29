""" 
String formating can be done using the format method
"""
""" before v6 """
# letter = "Hello sir, My name is {} and I'm from {}"
# letter = "Hello sir, My name is {1} and I'm from {0}"
name = "Prnce Sunsara"
country = "India"

# print(letter.format(name, country))
# print(letter.format(country, name))  # 1,0

""" after v6 f-string introduced"""
print(f"Hey, My name is {name} and I'm from {country}")