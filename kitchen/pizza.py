from abc import ABC, abstractmethod
from datetime import datetime

class Pizza(ABC):

    def __init__(self):
        self.cooked = True
        self.freshout_timestamp = datetime.now().timestamp()

    @abstractmethod
    def is_delicious(self):
        pass

    @abstractmethod
    def remove_ingredient(self, ingredient: str):
        pass

    @abstractmethod
    def add_ingredient(self, ingredient: str):
        pass