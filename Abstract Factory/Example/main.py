from abc import ABC
from enum import Enum


class DrinkType(Enum):
    TEA = 1
    COFFEE = 2

class HotDrink(ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print("Tea is delicious!")

class Coffee(HotDrink):
    def consume(self):
        print("Coffee is delicious!")

class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass

class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print("Boil water. Put {} ml of milk. Add tea leaves. Prepared!".format(amount))
        return Tea()

class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print("Boil water. Put {} ml of milk. Put coffee beans. Prepared!".format(amount))
        return Coffee()

# Regular Factory
def make_drink(drink_type):
    if drink_type == DrinkType.COFFEE:
        return CoffeeFactory().prepare(50)
    elif drink_type == DrinkType.TEA:
        return TeaFactory().prepare(100)
    else:
        return None

# Better way to have a Factory of Factories:

class MultiHotDrinkFactory:
    factories = dict()
    init_done = False

    def __init__(self):
        if not MultiHotDrinkFactory.init_done:
            MultiHotDrinkFactory.init_done = True
            for d in DrinkType:
                name = d.name[0] + d.name[1:].lower() + "Factory"
                factory_instance = eval(name)()
                MultiHotDrinkFactory.factories[d] = factory_instance

    def make_drink(self, drink_type, amount):
        if drink_type in self.factories:
            return self.factories[drink_type].prepare(amount)
        print("Invalid drink_type {}".format(drink_type))
        return None

if __name__ == "__main__":
    print("Old way of creation...")
    coffee = make_drink(DrinkType.COFFEE)
    tea = make_drink(DrinkType.TEA)
    print("----------------------------------")

    print("Create via MultiHotDrinkFactory...")
    coffee2 = MultiHotDrinkFactory().make_drink(DrinkType.COFFEE, 50)
    tea2 = MultiHotDrinkFactory().make_drink(DrinkType.TEA, 100)
    invalidDrink = MultiHotDrinkFactory().make_drink("Invalid", 400)