from TrafficAuthorityObserver import TrafficAuthority
from Person import Person

if __name__ == '__main__':
    p = Person("Abby", 14)
    ta = TrafficAuthority(p)

    print("Current Age: {}".format(p.age)) # Age is 14
    print("------------------------------------------------")

    print("Increasing current age: {} by 1: ".format(p.age))
    p.age = p.age + 1 # Age is 15. Can't drive
    print("Current Age: {}".format(p.age))  # Age is 14
    print("------------------------------------------------")

    print("Increasing current age: {} by 1: ".format(p.age))
    p.age = p.age + 1 # Age is 16. Can drive. Remove observer.
    print("Current Age: {}".format(p.age))  # Age is 14
    print("------------------------------------------------")

    print("Increasing current age: {} by 1: ".format(p.age))
    p.age = p.age + 1 # Age is 17. Nothing happens. Observer removed.
    print("Current Age: {}".format(p.age))  # Age is 14
