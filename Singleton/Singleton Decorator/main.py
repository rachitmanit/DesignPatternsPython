from Database import Database

if __name__ == "__main__":
    d1 = Database()
    d2 = Database()

    if d1 == d2:
        print("Identical object")

    print(d1)
    print(d2)
    print(Database())
    print(Database())
    print(Database())