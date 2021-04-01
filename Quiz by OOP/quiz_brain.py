class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_ans, current_question.answer)

    def check_answer(self, user_ans, correct_answer):
        if user_ans.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's Wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your Current Score is: {self.score}/{self.question_number}")
