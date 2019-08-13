import json
import random


class Question:

    def __init__(self, question, answers, right_answer):
        self.question = question
        self.answers = answers
        self.right_answer = right_answer

    def get_right_answer(self):
        return self.answers[self.right_answer - 1]


class Chat:

    with open('data.json') as f:
        raw_data = json.load(f)
        questions = []
        for q in raw_data:
            questions.append(Question(
                q['question'],
                q['answers'],
                q['right_answer']
            ))

    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.current_question = random.randint(0, len(Chat.questions) - 1)
        self.questions_left = [i for i in range(0, len(Chat.questions)) if i != self.current_question]

    def get_current_question(self):
        return Chat.questions[self.current_question]

    def update_question(self):
        self.current_question = random.choice(self.questions_left)
        del self.questions_left[self.questions_left.index(self.current_question)]

    def get_next_question(self):
        if not self.questions_left:
            self.current_question = None
            return None
        self.update_question()
        return self.get_current_question()
