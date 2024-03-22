'''
5. The Fitness Tracker
Objective:
The aim of this assignment is to create a program that tracks fitness activities and calories burned.

Task 1: Develop a function to log different fitness activities and their duration. For instance, 
activities = [’Dancing’, ‘Swimming’, ‘Biking’] and duration = [10, 20, 15] where Dancing corresponds to 10 minutes, 
Swimming corresponds to 20 minutes, and Biking corresponds to 15 minutes.

Task 2: Write a simple function that estimates calories burned based on the activity and duration. 
For instance, Total calories burned = Duration (in minutes)*3.5

Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.

'''

activities = ["dancing", "swimming", "biking"]
duration = [10, 20, 15]


def fitness_tracker(activities, durations):
    if len(activities) != len(durations):
      return "Both lists must have the same length."
    fitness_log = {}
    for i in range(len(activities)):
        fitness_log[activities[i]] = durations[i]
    return fitness_log
  
 
def calories_burned(duration):
  cals_each = [x *3.5 for x in duration]
  for count, cals in enumerate(cals_each):
     print(f"Workout {count + 1}: {cals} calories burned")
 
     
def summary(fitness_tracker):
  total_cals = sum(duration) *3.5

  cals_each = [x *3.5 for x in duration]
  summery_tracker = zip(activities, duration , cals_each)
  print(f"Total calories burned was {total_cals}.")
  for count, summery in enumerate(summery_tracker):
     print(f"{count +1}. Activity: {str.capitalize(summery[0])}: {summery[1]} minutes: Calorie burn of {summery[2]} calories!")
     
def best_fitness_tracker(user_input):   
  while True:
      user_choice = input("Would you like to [A]dd, [V]iew or [End]: ").upper()
      if user_choice == "A":
        user_choice1 = input("What activity do you want to add? ")
        user_choice2 = int(input("For how long? "))
        activities.append(user_choice1)
        duration.append(user_choice2)
      elif user_choice == "V":
        user_choice3 = input("Would you like to see [S]ummary, [C]alories, [T]racker? or [E]nd? " ).upper()
        if user_choice3 == "S":
          summary(fitness_tracker(activities,duration))
        elif user_choice3 == "C":
          calories_burned(duration)
        elif user_choice3 == "T":
          print(fitness_tracker(activities,duration))
        elif user_choice3 == "E":
          break
        else:
          print("Invalid input")
      elif user_choice == "E":
        break
      else:
        print("Invalid input")
  

while True:
  user_input = input("Are you ready to start logging your fitness? [Y/N] ").upper()
  if user_input == "Y":
    best_fitness_tracker(user_input)
  elif user_input == "N":
    print("Thank you come again!")
    break
  else:
    print("Invalid input!")