class Person:
    def __init__(self, first_name, last_name) -> None:
        self._first_name = first_name
        self._last_name = last_name
    
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
 
person = Person(first_name="Diego", last_name="Cortes")

print(person.first_name)
print(person.last_name)