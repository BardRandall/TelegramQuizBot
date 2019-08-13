import random
from questions import *


class Chat:

    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.current_question = random.randint(0, len(get_all()) - 1)
        self.questions_left = [i for i in range(0, len(get_all())) if i != self.current_question]

    def get_current_question(self):
        return get_by_id(self.current_question)

    def update_question(self):
        self.current_question = random.choice(self.questions_left)
        del self.questions_left[self.questions_left.index(self.current_question)]

    def get_next_question(self):
        if not self.questions_left:
            self.current_question = None
            return None
        self.update_question()
        return self.get_current_question()
