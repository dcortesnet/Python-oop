class Person:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        
person = Person(first_name="Diego", last_name="Cortes")

print(person) # <__main__.Person object at 0x000001E6DEF8E020>
