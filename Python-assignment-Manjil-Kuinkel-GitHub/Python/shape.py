from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area():
       return 0
    def display(self):
        print("This is concrete method")