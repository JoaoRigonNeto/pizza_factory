from abc import ABC, abstractmethod
from datetime import datetime

class Pizza(ABC):

    def __init__(self, ingredients: list):
        self.cooked = True
        self.freshout_timestamp = datetime.now().timestamp()
        self.ingredients = ingredients

    @abstractmethod
    def is_delicious(self):
        pass
