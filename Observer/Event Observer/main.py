from Person import Person
from Observers import *

if __name__ == '__main__':
    person = Person("Sherlock", "Bangalore, India")
    person.add_observer(call_doctor)
    person.catch_a_cold()
    print("------------------------")

    person.add_observer(print_ill)
    person.catch_a_cold()

    print("------------------------")
    person.remove_observer(call_doctor)
    person.catch_a_cold()