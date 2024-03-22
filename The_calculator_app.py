'''
1. The Calculator App
Objective:
The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

Task 1: Create functions for each arithmetic operation.
Task 2: Implement user input to receive numbers and an operation choice.
Task 3: Ensure your program can handle division by zero and other potential errors.
'''

# Task one 

# 1. define 4 functions one for adding, subtracting, multiplying, and division.
# 2. make a key word/ words for each function
# 3. define the operation within the the functions
#


def addition(users_numbers1, users_numbers2): 
  return users_numbers1 + users_numbers2


def subtraction(users_numbers1, users_numbers2):
  return users_numbers1 - users_numbers2


def multiplication(users_numbers1, users_numbers2):
  return users_numbers1 * users_numbers2


def division(users_numbers1, users_numbers2):
  if users_numbers2 or users_numbers1 == 0:
    return  users_numbers1 / users_numbers2
  else:
    return "You cant divide by zero."
  
# Task two.

# 1. make user inputs for numbers to be used
# 2. make a loop to give the users choices.3
def brains_of(user_choice):
  while True:
    
    users_numbers1 = float(input("Enter in a number: "))
    users_choice = input("Choose an action: [A]dd, [S]ubtract, [M]ultiply, [D]ivide or [E]nd  ").upper()
    users_numbers2 = float(input("Enter in a second number: "))
    if users_choice == "e":
      break
    elif users_choice == "A":
          total_addition = addition(users_numbers1, users_numbers2)
          result = total_addition
          print(f"Result: {total_addition:.4f}")
    elif users_choice == "S":
      total_subtraction = subtraction(users_numbers1, users_numbers2)
      result = total_subtraction
      print(f"Result: {total_subtraction:.4f}")
    elif users_choice == "M":
      total_multiplication = multiplication(users_numbers1, users_numbers2)
      result = total_multiplication
      print(f"Result: {total_multiplication:.4f}")
    elif users_choice == "D":
      total_division = division(users_numbers1, users_numbers2)
      result = total_division
      print(f"Result: {total_division}")
    else:
      print("Invalid input!")


while True:
  user_choice = input("Are you ready to start? [Y/N] ").upper()
  if user_choice == "Y":
    brains_of(user_choice)
  elif user_choice == "N":
    print("Thank you come again!")
    break
  else:
    print("Invalid input!")