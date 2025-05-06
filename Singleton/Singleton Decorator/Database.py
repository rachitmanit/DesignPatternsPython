import random
from Singleton import Singleton

@Singleton
class Database:
    def __init__(self):
        self._id = random.randint(0, 100)
        print("Creating Data object")

    def __str__(self):
        return "Database ID: {}".format(self._id)
