class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, value):
        self.first_name, self.last_name = value.split(" ")

person = Person("Diego", "Cortes")
person.full_name = "Juan Cortes"
print(person.full_name)  # Output: Juan Cortes