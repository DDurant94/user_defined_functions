'''
The Quiz Game
Objective:
The aim of this assignment is to create a quiz game that asks questions and checks answers.

Task 1: Develop a list of questions and answers.
Task 2: Write a function that quizzes the user and takes their answers.
Task 3: Score the quiz and give the user feedback on their performance.
'''
# make 2 lists one for questions and one for answers
# make a function that takes in answers as well as gives questions



questions = [{"question":"What is the color of the sky?", "answer": "blue"}, 
             {"question":"How many hours are in a day?", "answer": "24"}, 
             {"question":"How many days are in a year?", "answer": "365"},
             {"question":"Do dogs bark?", "answer": "yes"}]


def user_quiz(questions):
  score = 0 
  total_questions = len(questions)
  for question in questions:
    users_choice = input(f"{question["question"]} answer: ").lower()
    if users_choice == question["answer"]:
      print(f"You answer right!")
      score += 1 
    else:
      print(f"You got the wrong answer. The right answer is {question["answer"]}.")
  print(f"Your score was {score}/{total_questions}")



user_quiz(questions)