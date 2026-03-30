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

# age = int(input("Enter your age: "))
# gender = input("Enter your gender: ").lower()

# if age > 18 and gender == "male":
#     print("You are eligible for the ride.")
# elif age > 18 and gender == "female":
#     print("Females, are not allowed for the ride.")
# else:
#     print("You are not eligible for the ride.")

# Marksheet

Eng = int(input("Enter English Marks: "))
Isl = int(input("Enter Islamiate Marks: "))
Math = int(input("Enter Maths Marks: "))
Urdu = int(input("Enter Urdu Marks: "))
Comp = int(input("Enter Computer Marks: "))

obtain = Eng + Isl + Math + Urdu + Comp
percentage = obtain / 500 * 100

if percentage >= 80 and percentage <= 100:
    print("A-One Grade")
elif percentage >= 70 and percentage < 80:
    print("A Grade")
elif percentage >= 60 and percentage < 70:
    print("B Grade")
elif percentage >= 50 and percentage < 60:
    print("C Grade")
elif percentage >= 40 and percentage < 50:
    print("D Grade")
elif percentage >= 0 and percentage < 40:
    print("Fail")
else:
    print("Fail")



