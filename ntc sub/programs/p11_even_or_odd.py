# Program 11 - Even or Odd
# Attempt 1 (wrong logic - checking >= 0 instead of == 0)
# num = int(input("give your number to test even odd : "))
# num1 = num / 2
# if num1 >= 0:
#     print("your number is even")
# else:
#     print("its odd")

# Attempt 2 (missing indentation + wrong condition)
# num = int(input("give your number to test even odd : "))
# if num % 2:
# print("your number is even")
# else:
# print("its odd")

# Still working on this one...
num = int(input("give your number to test even odd : "))
if num % 2 == 0:
    print(f"your number is even")
else:
    print(f"its odd")
