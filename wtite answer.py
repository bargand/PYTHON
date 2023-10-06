
# def calculate_costings(earned_marks):
#     total_costings = 25
#     correct_costings = (earned_marks + total_costings) // 4
#     wrong_costings = total_costings - correct_costings
#     return correct_costings, wrong_costings

# # Example usage:
# total_marks = 41
# correct, wrong = calculate_costings(total_marks)
# print(f"Number of correct costings: {correct}")
# print(f"Number of wrong costings: {wrong}")

# def calculate_costings(correct_score):
#     total_costings = 25
#     max_score = total_costings * 3
#     wrong_score = max_score - correct_score

#     correct_costings = correct_score // 3
#     wrong_costings = total_costings - correct_costings

#     return correct_costings, wrong_costings

# total_score = 41
# correct, wrong = calculate_costings(total_score)
# print(f"Number of correct costings: {correct}")
# print(f"Number of wrong costings: {wrong}")

# def Calculation(total_score):
#     MaxCorrect = total_score // 3
#     CorrectAns = min(MaxCorrect, 25)  # There are 25 costings in total
#     WrongAns = 25 - CorrectAns

#     return CorrectAns, WrongAns

# total_score = 55
# correct, wrong = Calculation(total_score)
# print(f"Number of correct costings: {correct}")
# print(f"Number of wrong costings: {wrong}")

# def main():
#     total_questions = 25
#     correct_marks = 3
#     incorrect_marks = -1
#     target_score = 41

#     # Initialize variables to keep track of correct and wrong answers
#     correct_answers = 0
#     wrong_answers = 0

#     # Iterate through each question
#     for _ in range(total_questions):
#         answer = input("Enter your answer (1 for correct, 0 for incorrect): ")
#         if answer == "1":
#             correct_answers += 1
#         elif answer == "0":
#             wrong_answers += 1
#         else:
#             print("Invalid input. Please enter 1 for correct or 0 for incorrect.")

#     # Calculate the total score
#     total_score = (correct_answers * correct_marks) + (wrong_answers * incorrect_marks)

#     # Display the results
#     print(f"Total score: {total_score}")
#     print(f"Correct answers: {correct_answers}")
#     print(f"Wrong answers: {wrong_answers}")

#     # Check if the calculated total score matches the target score
#     if total_score == target_score:
#         print("Congratulations! Your score matches the target score.")
#     else:
#         print("Your score does not match the target score.")

# if __name__ == "__main__":
#     main()


# def calculate_correct_wrong(total_marks):
#     total_questions = 25
#     marks_per_question = 3
#     negative_marks = -1

#     # Calculate the maximum possible marks if all questions are correct
#     max_possible_marks = total_questions * marks_per_question

#     # Calculate the number of correct questions
#     correct_questions = (total_marks - (total_questions * negative_marks)) // marks_per_question

#     # Calculate the number of wrong questions
#     wrong_questions = total_questions - correct_questions

#     return correct_questions, wrong_questions

# # Enter the total marks obtained by the student
# total_marks_obtained = 41

# # Call the function to calculate correct and wrong questions
# correct, wrong = calculate_correct_wrong(total_marks_obtained)

# print("Number of correct questions:", correct)
# print("Number of wrong questions:", wrong)


# def main():
#     total_marks = 75
#     marks_per_question = 3
#     penalty_per_wrong_answer = -1
#     total_questions = 25

#     # Calculate maximum possible score
#     max_possible_score = total_questions * marks_per_question

#     # Calculate the number of correct answers
#     correct_answers = (total_marks - max_possible_score) // penalty_per_wrong_answer

#     # Calculate the number of wrong answers
#     wrong_answers = total_questions - correct_answers

#     print("Number of correct answers:", correct_answers)
#     print("Number of wrong answers:", wrong_answers)

# if __name__ == "__main__":
#     main()


# def main():
#     total_score = 41
#     marks_per_question = 3
#     penalty_per_wrong_answer = -1
#     total_questions = 25

#     # Calculate the maximum possible score
#     max_possible_score = total_questions * marks_per_question

#     # Calculate the number of correct answers
#     correct_answers = (total_score - max_possible_score) / (marks_per_question + penalty_per_wrong_answer)

#     # Calculate the number of wrong answers
#     wrong_answers = total_questions - correct_answers

#     print("Number of correct answers:", int(correct_answers))
#     print("Number of wrong answers:", int(wrong_answers))

# if __name__ == "__main__":
#     main()


# def calculate_answers(total_marks, marks_per_question, penalty_per_wrong_answer, total_questions):
#     # Calculate the maximum possible score
#     max_possible_score = total_questions * marks_per_question

#     # Calculate the number of correct answers
#     correct_answers = (total_marks - max_possible_score) // penalty_per_wrong_answer

#     # Calculate the number of wrong answers
#     wrong_answers = total_questions - correct_answers

#     return correct_answers, wrong_answers

# def main():
#     total_marks = 41
#     marks_per_question = 3
#     penalty_per_wrong_answer = -1
#     total_questions = 25

#     correct_answers, wrong_answers = calculate_answers(total_marks, marks_per_question, penalty_per_wrong_answer, total_questions)

#     print("Number of correct answers:", correct_answers)
#     print("Number of wrong answers:", wrong_answers)

# if __name__ == "__main__":
#     main()


def get_correct_and_wrong_questions(total_marks, marks_per_question):
  """
  Gets the number of correct and wrong questions for a given total marks and marks per question.

  Args:
    total_marks: The total marks obtained in the exam.
    marks_per_question: The marks per question.

  Returns:
    A tuple of the number of correct questions and the number of wrong questions.
  """

  number_of_correct_questions = total_marks // marks_per_question
  number_of_wrong_questions = total_marks - number_of_correct_questions * marks_per_question
  return number_of_correct_questions, number_of_wrong_questions


if __name__ == "__main__":
  number_of_correct_questions, number_of_wrong_questions = get_correct_and_wrong_questions(60, 3)
  print("Number of correct questions:", number_of_correct_questions)
  print("Number of wrong questions:", number_of_wrong_questions)
