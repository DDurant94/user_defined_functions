'''
3. The Grade Analyzer
Objective:
The aim of this assignment is to analyze a set of grades and provide statistics.

Task 1: Code a function to calculate the average grade.
Task 2: Implement a function to find the highest and lowest grade.
Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).
'''

# make a empty list to store grades (add/remove) later
# make a function to find the average grade in the list


def average_grade(grades):
  average = sum(grades) / len(grades)
  print(f"The average of across the whole class is {average:.2f}.")

def high_low_grade(grades):
   mx = max(grades) 
   mn = min(grades)
   print(f"The highest grade in the class is {mx} and the lowest grade in the class was {mn}.")

def adding_letters(grades):
  letter_grades=[]
  for grade in grades:
    if grade >= 90:
      letter_grades.append("A")
    elif grade >= 80:
      letter_grades.append("B")
    elif grade >= 70:
      letter_grades.append("C")
    elif grade >= 60:
      letter_grades.append("D")
    elif grade >=0:
      letter_grades.append("F")
  for letter in letter_grades:
    print(f"The scores have been updated to {letter}")

def list_of_grades(grades):
  for grade in grades:
    print(f"{grade}")
  
  



grades = []

while True:
  users_choice = input("Do you want to [A]dd, [R]emove, [V]iew, [E]xit? ").upper()

  if users_choice == "A":
    grades_to_add = int(input("How many grades do you want to add? "))
    for i in range(grades_to_add):
      grades_added = int(input(f"Enter in grades one at a time: \n {i+1}. "))
      grades.append(grades_added)

  elif users_choice == "R":
    grades_to_remove = int(input("How many grades do you want to remove? "))
    for i in range(grades_to_remove):
      grades_removed = int(input(f"Enter in grades one at a time: \n {i+1}. "))
      grades.append(grades_removed)
  elif users_choice == "V":
    while True:
      users_choice2 = input("Do you want to view [A]verage, [H]ighest/lowest, [L]ist or [E]xit ").upper()
      if users_choice2 == "A":
        average_grade(grades)
      elif users_choice2 == "H":
        high_low_grade(grades)
      elif users_choice2 == "L":
        while True:
          users_choice3 = input("Do you want to see [S]cores, [L]etter, [B]oth or [E]xit? ").upper()
          if users_choice3 == "S":
            list_of_grades(grades)
          elif users_choice3 == "L":
            adding_letters(grades)
            list_of_grades(grades)
          elif users_choice3 == "B":
            pass
          elif users_choice3 == "E":
            break
      elif users_choice2 == "E":
        break
      else:
        print("Invalid input")
  elif users_choice == "E":
    break





letter_grades = ["A" if x > 89 else "B" if x <= 89 and x > 79 else "C" if x <= 79 and x > 69 else "D" if x <= 69 and x > 59 else "F" for x in grades]