import json


class Question:

    def __init__(self, question, answers, right_answer):
        self.question = question
        self.answers = answers
        self.right_answer = right_answer

    def get_right_answer(self):
        return self.answers[self.right_answer - 1]


questions = []
with open('data.json') as f:
    raw_data = json.load(f)
    for q in raw_data:
        questions.append(Question(
            q['question'],
            q['answers'],
            q['right_answer']
        ))


def get_all():
    return questions


def get_by_id(index):
    return questions[index]
