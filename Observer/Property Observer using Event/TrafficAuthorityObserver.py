class TrafficAuthority:
    def __init__(self, person):
        self.person = person
        self.person.add_observer(self.can_drive)

    def can_drive(self, name, value):
        if name == 'age':
            if value < 16:
                print("You still can not drive.")
            else:
                print("Okay. You can drive")
                self.person.remove_observer(self.can_drive)
