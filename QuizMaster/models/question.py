from abc import ABC


class Question(ABC):
    """
    docstring
    """
    #TODO: add id
    def __init__(self, text, difficulty, category, created_by):
        """
        docstring
        """
        pass

    def display(self, id):
        pass

    def check_answer(self, my_answer):
        pass
