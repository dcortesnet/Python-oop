class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

person = Person("Diego", "Cortes")
print(person.full_name)  # Output: Diego Cortes