from PropertyObservable import PropertyObservable

class Person(PropertyObservable):
    def __init__(self, name, age):
        super().__init__()
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if self._age == age:
            return
        self._age = age
        self.call_on_status_changed("age", age)
