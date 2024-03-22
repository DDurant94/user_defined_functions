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

activities = ["Dancing", "Swimming", "Biking"]
duration = [10, 20, 15]


def fitness_tracker(activities, durations):
    if len(activities) != len(durations):
      return "Both lists must have the same length."
    fitness_log = {}
    for i in range(len(activities)):
        fitness_log[activities[i]] = durations[i]
    return fitness_log
  
 

def calories_burned(duration):
   for time in duration:
      time *= 3.5
      return time

  

def summary(fitness_log):
   pass
   


while True:
    user_choice = input("Would you like to [A]dd, [V]iew or [End]: ").upper()
    if user_choice == "A":
      user_choice1 = input("What activity do you want to add? ")
      user_choice2 = int(input("For how long? "))
      activities.append(user_choice1)
      duration.append(user_choice2)
    elif user_choice == "V":
       print(calories_burned(duration))
       print(fitness_tracker(activities,duration))
       

      
    elif user_choice == "E":
       break
    else:
       print("Invalid input")