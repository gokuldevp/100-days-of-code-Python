class QuestionBrain:
    def __init__(self, que_list):
        # self.current_question = None
        self.question_number = 0
        self.question_list = que_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q{self.question_number}: {current_question.text} (True/False): ").title()
        
        def check_answer():
            return current_question.answer == user_input
        if check_answer():
            print(f"Your answer is right.")
            self.score += 1
        else:
            print(f"Your answer is wrong.")
        print(f"The correct answer was: {current_question.answer}")
        print(f"Your score is {self.score}/{self.question_number}\n")
        check_answer()

    def still_have_question(self):
        return self.question_number < len(self.question_list)

