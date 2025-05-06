from Event import Event

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.__fall_ill = Event()

    def add_observer(self, observer):
        self.__fall_ill.append(observer)

    def remove_observer(self, observer):
        if observer in self.__fall_ill:
            self.__fall_ill.remove(observer)

    def catch_a_cold(self):
        self.__fall_ill(self.name, self.address)
