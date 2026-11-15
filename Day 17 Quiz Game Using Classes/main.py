from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item['text'] , item['answer']))

quiz_game = QuizBrain(question_bank)

while(quiz_game.still_has_question()):  
    quiz_game.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz_game.score}/{quiz_game.question_number} ")