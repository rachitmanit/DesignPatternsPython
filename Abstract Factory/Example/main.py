from DrinkType import DrinkType
from DrinkFactory import make_drink, MultiHotDrinkFactory

if __name__ == "__main__":
    print("Old way of creation...")
    coffee = make_drink(DrinkType.COFFEE)
    tea = make_drink(DrinkType.TEA)
    print("----------------------------------")

    print("Create via MultiHotDrinkFactory...")
    coffee2 = MultiHotDrinkFactory().make_drink(DrinkType.COFFEE, 50)
    tea2 = MultiHotDrinkFactory().make_drink(DrinkType.TEA, 100)
    invalidDrink = MultiHotDrinkFactory().make_drink("Invalid", 400)