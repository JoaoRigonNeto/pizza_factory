from abc import ABC, abstractmethod
from datetime import datetime

class Pizza(ABC):

    def __init__(self):
        self.freshout_timestamp = datetime.now().timestamp()
        self.basic_ingredients = ["dough"]
        self.ingredients = []

    @abstractmethod
    def is_delicious(self):
        pass

    @abstractmethod
    def remove_ingredient(self, ingredient: str):
        pass
