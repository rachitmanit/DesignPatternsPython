class Journal(object):
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, entry):
        self.count += 1
        self.entries.append(entry)

    def remove_entry(self, entry):
        self.count -= 1
        if entry in self.entries:
            self.entries.remove(entry)

    def __str__(self):
        return "Entries count: {} \nEntries: {}".format(self.count, self.entries)

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, 'w') as fp:
            fp.write(journal)


journal = Journal()
journal.add_entry("I ate a bug.")
journal.add_entry("I smiled today.")
journal.add_entry("I laughed today.")

print(journal)

print("-------------------")

journal.remove_entry("I ate a bug")
print(journal)

print("-------------------")

journal.remove_entry("I ate a bug.")
print(journal)

print("-------------------")
print("Creating file: ")
PersistenceManager.save_to_file(journal.__str__(), "journal.txt")