from abc import ABC

class HotDrink(ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print("Tea is delicious!")

class Coffee(HotDrink):
    def consume(self):
        print("Coffee is delicious!")