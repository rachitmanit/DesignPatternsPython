from abc import ABC
from Drink import Tea, Coffee
from DrinkType import DrinkType

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