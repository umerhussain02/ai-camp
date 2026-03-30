# name =  "alishbaaaaaaaaa"
# name =  'alishba bori'
# print(name)

# Ambiguity of data
# a =  8 * 4 / 2 + 5 - 3
# a =  8 * 4 / (2 + (5 - 3))
# print(a)

# x =  int(input("Enter value: "))
# y = 6
# z = x + y
# print(z)

# Comparisition Operators
# Equal to ==
# Lessthan and equal to <=
# Graterthan and equal to >=
# Not equal to !=
# Not !

# Conditional statement

# a = 5
# if a < 3:
#     print("Good")
# # elif a == 5:
# elif a != 5:
#     print("Woww")
# else:
#     print("Bad")

# Logical Operators
# or (If one condition is true)
# and (All conditions has to be true)
# not !

age = int(input("Enter your age: "))
gender = input("Enter your gender: ").lower()

if age > 18 and gender == "male":
    print("You are eligible for the ride.")
elif age > 18 and gender == "female":
    print("Females, are not allowed for the ride.")
else:
    print("You are not eligible for the ride.")
