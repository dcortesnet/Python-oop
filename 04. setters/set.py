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
    
    @first_name.setter
    def first_name(self, new_first_name):
        self._first_name = new_first_name
        
    @last_name.setter
    def last_name(self, new_last_name):
        self._last_name = new_last_name
 
person = Person(first_name="Diego", last_name="Cortes")

print(person.first_name)
print(person.last_name)

person.first_name = "Juan"
person.last_name = "Escandon"

print(person.first_name)
print(person.last_name)